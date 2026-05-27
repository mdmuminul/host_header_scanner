#!/usr/bin/env python3
"""
Host Header Research Tool v2
General-purpose Host header validation tester and report generator.

Purpose:
- Test one domain, one URL, or a list of domains.
- Compare normal Host header vs arbitrary invalid Host header.
- Detect weak Host validation.
- Detect possible Host header injection signals.
- Avoid false positives from server-generated Apache/Nginx footer reflection.
- Generate JSON, CSV, Markdown, and HTML reports.

Ethical scope:
- Only performs GET requests.
- Does not log in.
- Does not test password reset poisoning.
- Does not perform cache poisoning.
- Does not perform DNS rebinding.
- Intended for academic measurement and defensive analysis.
"""

import argparse
import asyncio
import csv
import hashlib
import html
import json
import re
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse

import aiohttp


# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------

DEFAULT_FAKE_HOST = "attacker.com"
DEFAULT_USER_AGENT = (
    "HostHeaderResearchTool/2.0 "
    "(academic research; non-invasive GET requests)"
)
DEFAULT_TIMEOUT = 10
DEFAULT_CONCURRENCY = 5
DEFAULT_BODY_LIMIT = 250_000
DEFAULT_SIMILARITY_THRESHOLD = 0.90

REJECT_STATUS_CODES = {400, 403, 404, 421, 444}
REDIRECT_STATUS_CODES = {301, 302, 303, 307, 308}


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

@dataclass
class ProbeResult:
    scheme: str
    url: str
    host_header: str
    status: Optional[int]
    final_url: str
    headers: Dict[str, str]
    body_hash: str
    body_length: int
    body_snippet: str
    error: str


@dataclass
class HostHeaderFinding:
    target: str
    tested_url: str
    scheme: str
    real_host: str
    fake_host: str

    baseline_status: Optional[int]
    invalid_status: Optional[int]

    baseline_final_url: str
    invalid_final_url: str

    baseline_hash: str
    invalid_hash: str
    baseline_body_length: int
    invalid_body_length: int

    content_same_hash: bool
    content_similarity: float

    fake_host_reflected_in_headers: bool
    fake_host_reflected_in_body: bool
    fake_host_reflected_in_location: bool
    fake_host_reflected_in_cookie: bool
    fake_host_reflection_only_server_footer: bool

    classification: str
    risk_level: str
    interpretation: str
    recommendation: str

    baseline_error: str
    invalid_error: str
    tested_at: str


# ---------------------------------------------------------------------------
# General helpers
# ---------------------------------------------------------------------------

def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize_domain(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"^https?://", "", value)
    value = value.split("/")[0]
    value = value.split(":")[0]
    return value


def parse_target(value: str, default_scheme: str = "https") -> Tuple[str, str, str]:
    """
    Returns:
      scheme, host, url

    Input can be:
      example.ee
      https://example.ee/
      https://example.ee/path
    """
    value = value.strip()

    if not value.startswith(("http://", "https://")):
        host = normalize_domain(value)
        return default_scheme, host, f"{default_scheme}://{host}/"

    parsed = urlparse(value)
    scheme = parsed.scheme or default_scheme
    host = parsed.hostname or normalize_domain(value)
    path = parsed.path or "/"
    query = f"?{parsed.query}" if parsed.query else ""

    url = f"{scheme}://{host}{path}{query}"
    return scheme, host, url


def normalize_body(body: str) -> str:
    """
    Reduces dynamic noise before hashing/comparison.
    """
    body = body.lower()
    body = re.sub(r"\s+", " ", body)
    body = re.sub(r"[a-f0-9]{32,}", "<hex>", body)
    body = re.sub(r"\b\d{10,}\b", "<number>", body)
    body = re.sub(r"\d{4}-\d{2}-\d{2}", "<date>", body)
    body = re.sub(r"\d{2}:\d{2}:\d{2}", "<time>", body)
    body = re.sub(r"nonce=\"[^\"]+\"", "nonce=\"<nonce>\"", body)
    body = re.sub(r"csrf[^=]*=[\"'][^\"']+[\"']", "csrf='<csrf>'", body)
    return body.strip()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()


def body_similarity(a: str, b: str) -> float:
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0

    a = a[:DEFAULT_BODY_LIMIT]
    b = b[:DEFAULT_BODY_LIMIT]
    return round(SequenceMatcher(None, a, b).ratio(), 4)


def headers_to_text(headers: Dict[str, str]) -> str:
    return "\n".join(f"{k}: {v}" for k, v in headers.items())


def get_header(headers: Dict[str, str], header_name: str) -> str:
    for key, value in headers.items():
        if key.lower() == header_name.lower():
            return value
    return ""


# ---------------------------------------------------------------------------
# False-positive reduction for server-generated pages
# ---------------------------------------------------------------------------

def reflection_is_only_server_generated_page(body: str, fake_host: str) -> bool:
    """
    Detect harmless reflection caused by default web-server generated pages.

    Example:
      <address>Apache/2.4.67 (Debian) Server at attacker.com Port 80</address>

    This is not application-level Host header injection by itself.
    It should not be classified as possible Host header injection unless the fake Host
    appears in a security-relevant location such as:
      - Location header
      - Set-Cookie header
      - application-generated absolute URL
      - password reset URL
      - canonical URL
      - form action URL
    """
    if not body:
        return False

    body_low = body.lower()
    fake_low = fake_host.lower()

    if fake_low not in body_low:
        return False

    idx = body_low.find(fake_low)
    context = body_low[max(0, idx - 400): idx + 400]

    harmless_patterns = [
        # Apache footer
        r"server at\s+" + re.escape(fake_low),
        r"server at\s+" + re.escape(fake_low) + r"\s+port\s+\d+",
        r"<address>.*server at.*port.*</address>",

        # Apache generated pages
        r"apache/[0-9.]+",
        r"apache server at",
        r"the document has moved",
        r"moved permanently",
        r"found",
        r"bad request",
        r"forbidden",
        r"not found",
        r"misdirected request",

        # Nginx default pages
        r"<center>nginx</center>",
        r"nginx/[0-9.]+",
        r"<hr><center>nginx",

        # Common generated titles
        r"<title>301 moved permanently</title>",
        r"<title>302 found</title>",
        r"<title>400 bad request</title>",
        r"<title>403 forbidden</title>",
        r"<title>404 not found</title>",
        r"<title>421 misdirected request</title>",
    ]

    for pattern in harmless_patterns:
        if re.search(pattern, context, re.IGNORECASE | re.DOTALL):
            return True

    return False


def body_contains_security_relevant_fake_host(body: str, fake_host: str) -> bool:
    """
    Detect stronger application-level reflection signals in successful responses.

    This is intentionally conservative. It looks for the fake Host inside places that
    commonly matter for Host header injection.
    """
    if not body:
        return False

    fake = re.escape(fake_host)
    patterns = [
        # Absolute URLs
        rf"https?://{fake}",
        rf"//{fake}",

        # HTML attributes
        rf'href=["\']https?://{fake}',
        rf'src=["\']https?://{fake}',
        rf'action=["\']https?://{fake}',
        rf'formaction=["\']https?://{fake}',

        # Canonical / metadata
        rf'rel=["\']canonical["\'][^>]+{fake}',
        rf'property=["\']og:url["\'][^>]+{fake}',
        rf'name=["\']twitter:url["\'][^>]+{fake}',

        # JSON-ish generated URLs
        rf'"url"\s*:\s*"https?://{fake}',
        rf'"baseurl"\s*:\s*"https?://{fake}',
        rf'"base_url"\s*:\s*"https?://{fake}',
    ]

    for pattern in patterns:
        if re.search(pattern, body, re.IGNORECASE | re.DOTALL):
            return True

    return False


# ---------------------------------------------------------------------------
# Input loading
# ---------------------------------------------------------------------------

def load_targets_from_file(
    path: str,
    tld_filter: Optional[str],
    limit: Optional[int],
) -> List[str]:
    """
    Supports:
    - Tranco CSV: rank,domain
    - Plain text: one domain or URL per line
    """
    p = Path(path)

    if not p.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    lines = p.read_text(encoding="utf-8", errors="ignore").splitlines()
    clean_lines = [
        line.strip()
        for line in lines
        if line.strip() and not line.strip().startswith("#")
    ]

    if not clean_lines:
        return []

    first = clean_lines[0]
    first_parts = first.split(",")

    targets: List[str] = []
    is_tranco = len(first_parts) >= 2 and first_parts[0].strip().isdigit()

    if is_tranco:
        rows = []

        with open(path, newline="", encoding="utf-8", errors="ignore") as f:
            reader = csv.reader(f)

            for row in reader:
                if len(row) < 2:
                    continue

                rank_raw = row[0].strip()
                domain = row[1].strip().lower()

                if not rank_raw.isdigit():
                    continue

                if tld_filter and not domain.endswith(tld_filter.lower()):
                    continue

                rows.append((int(rank_raw), domain))

        rows.sort(key=lambda x: x[0])
        targets = [domain for _, domain in rows]

    else:
        for line in clean_lines:
            target = line.strip()

            if tld_filter:
                domain = normalize_domain(target)
                if not domain.endswith(tld_filter.lower()):
                    continue

            targets.append(target)

    if limit:
        targets = targets[:limit]

    return targets


# ---------------------------------------------------------------------------
# Network probing
# ---------------------------------------------------------------------------

async def fetch_once(
    session: aiohttp.ClientSession,
    url: str,
    host_header: str,
    timeout: int,
    user_agent: str,
    body_limit: int,
) -> ProbeResult:
    parsed = urlparse(url)
    scheme = parsed.scheme

    headers = {
        "Host": host_header,
        "User-Agent": user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "close",
    }

    try:
        async with session.get(
            url,
            headers=headers,
            timeout=aiohttp.ClientTimeout(total=timeout),
            allow_redirects=False,
            ssl=False,
        ) as response:
            body_bytes = await response.content.read(body_limit)
            charset = response.charset or "utf-8"

            try:
                body = body_bytes.decode(charset, errors="ignore")
            except LookupError:
                body = body_bytes.decode("utf-8", errors="ignore")

            normalized = normalize_body(body)

            return ProbeResult(
                scheme=scheme,
                url=url,
                host_header=host_header,
                status=response.status,
                final_url=str(response.url),
                headers=dict(response.headers),
                body_hash=sha256_text(normalized),
                body_length=len(body),
                body_snippet=body[:5000],
                error="",
            )

    except Exception as e:
        return ProbeResult(
            scheme=scheme,
            url=url,
            host_header=host_header,
            status=None,
            final_url="",
            headers={},
            body_hash="",
            body_length=0,
            body_snippet="",
            error=f"{type(e).__name__}: {str(e)[:200]}",
        )


async def test_target(
    semaphore: asyncio.Semaphore,
    session: aiohttp.ClientSession,
    target: str,
    fake_host: str,
    schemes: List[str],
    timeout: int,
    user_agent: str,
    body_limit: int,
    similarity_threshold: float,
    probe_gap: float,
) -> List[HostHeaderFinding]:
    findings: List[HostHeaderFinding] = []

    async with semaphore:
        for scheme in schemes:
            original_scheme, real_host, parsed_url = parse_target(target, default_scheme=scheme)

            # If the user gave a full URL and only one scheme is requested,
            # keep the original URL scheme and path.
            if target.startswith(("http://", "https://")) and len(schemes) == 1:
                url = parsed_url
                scheme = original_scheme
            else:
                parsed = urlparse(parsed_url)
                path = parsed.path or "/"
                query = f"?{parsed.query}" if parsed.query else ""
                url = f"{scheme}://{real_host}{path}{query}"

            baseline = await fetch_once(
                session=session,
                url=url,
                host_header=real_host,
                timeout=timeout,
                user_agent=user_agent,
                body_limit=body_limit,
            )

            await asyncio.sleep(probe_gap)

            invalid = await fetch_once(
                session=session,
                url=url,
                host_header=fake_host,
                timeout=timeout,
                user_agent=user_agent,
                body_limit=body_limit,
            )

            finding = analyze_pair(
                target=target,
                tested_url=url,
                scheme=scheme,
                real_host=real_host,
                fake_host=fake_host,
                baseline=baseline,
                invalid=invalid,
                similarity_threshold=similarity_threshold,
            )

            findings.append(finding)

    return findings


# ---------------------------------------------------------------------------
# Analysis / classification
# ---------------------------------------------------------------------------

def analyze_pair(
    target: str,
    tested_url: str,
    scheme: str,
    real_host: str,
    fake_host: str,
    baseline: ProbeResult,
    invalid: ProbeResult,
    similarity_threshold: float,
) -> HostHeaderFinding:
    baseline_body_norm = normalize_body(baseline.body_snippet)
    invalid_body_norm = normalize_body(invalid.body_snippet)

    same_hash = bool(baseline.body_hash and baseline.body_hash == invalid.body_hash)
    sim = body_similarity(baseline_body_norm, invalid_body_norm)

    fake_low = fake_host.lower()

    invalid_headers_text = headers_to_text(invalid.headers).lower()
    invalid_body_low = invalid.body_snippet.lower()

    location = get_header(invalid.headers, "Location").lower()
    set_cookie = get_header(invalid.headers, "Set-Cookie").lower()

    reflected_headers_raw = fake_low in invalid_headers_text
    reflected_location = fake_low in location or fake_low in invalid.final_url.lower()
    reflected_cookie = fake_low in set_cookie
    reflected_body_raw = fake_low in invalid_body_low

    only_server_footer = reflection_is_only_server_generated_page(
        invalid.body_snippet,
        fake_host,
    )

    security_relevant_body_reflection = body_contains_security_relevant_fake_host(
        invalid.body_snippet,
        fake_host,
    )

    reflected_body_dangerous = (
        reflected_body_raw
        and invalid.status is not None
        and 200 <= invalid.status < 400
        and not only_server_footer
        and security_relevant_body_reflection
    )

    # Headers are only treated as important if not merely part of harmless server-generated text.
    # Location and Set-Cookie are checked separately and always considered stronger signals.
    reflected_headers = reflected_headers_raw

    classification, risk_level, interpretation, recommendation = classify(
        baseline=baseline,
        invalid=invalid,
        same_hash=same_hash,
        similarity=sim,
        similarity_threshold=similarity_threshold,
        reflected_headers=reflected_headers,
        reflected_body_dangerous=reflected_body_dangerous,
        reflected_location=reflected_location,
        reflected_cookie=reflected_cookie,
        only_server_footer=only_server_footer,
    )

    return HostHeaderFinding(
        target=target,
        tested_url=tested_url,
        scheme=scheme,
        real_host=real_host,
        fake_host=fake_host,

        baseline_status=baseline.status,
        invalid_status=invalid.status,

        baseline_final_url=baseline.final_url,
        invalid_final_url=invalid.final_url,

        baseline_hash=baseline.body_hash,
        invalid_hash=invalid.body_hash,
        baseline_body_length=baseline.body_length,
        invalid_body_length=invalid.body_length,

        content_same_hash=same_hash,
        content_similarity=sim,

        fake_host_reflected_in_headers=reflected_headers,
        fake_host_reflected_in_body=reflected_body_dangerous,
        fake_host_reflected_in_location=reflected_location,
        fake_host_reflected_in_cookie=reflected_cookie,
        fake_host_reflection_only_server_footer=only_server_footer,

        classification=classification,
        risk_level=risk_level,
        interpretation=interpretation,
        recommendation=recommendation,

        baseline_error=baseline.error,
        invalid_error=invalid.error,
        tested_at=now_utc(),
    )


def classify(
    baseline: ProbeResult,
    invalid: ProbeResult,
    same_hash: bool,
    similarity: float,
    similarity_threshold: float,
    reflected_headers: bool,
    reflected_body_dangerous: bool,
    reflected_location: bool,
    reflected_cookie: bool,
    only_server_footer: bool,
) -> Tuple[str, str, str, str]:

    if baseline.error and invalid.error:
        return (
            "Inconclusive",
            "Unknown",
            "Both the baseline request and invalid Host request failed. The target could not be tested reliably.",
            "Retest manually from another network or with a longer timeout.",
        )

    if baseline.error and not invalid.error:
        return (
            "Inconclusive",
            "Unknown",
            "The baseline request failed but the invalid Host request returned a response. This result is not reliable.",
            "Retest manually and verify whether the original website is reachable.",
        )

    if invalid.error:
        return (
            "Inconclusive",
            "Low",
            "The invalid Host request failed. This may indicate rejection, timeout, CDN filtering, or network failure.",
            "Retest manually. If invalid Host consistently fails while baseline succeeds, treat this as likely validation/filtering.",
        )

    # Strong Host header injection signals.
    if reflected_location:
        return (
            "Possible Host header injection",
            "High",
            "The injected Host value appeared in the redirect Location header or final URL. This suggests possible redirect poisoning or Host header injection.",
            "Manually verify the redirect. Configure redirects to use a fixed canonical hostname, not the request Host header.",
        )

    if reflected_cookie:
        return (
            "Possible Host header injection",
            "High",
            "The injected Host value appeared in the Set-Cookie header. This suggests response construction from an untrusted Host value.",
            "Validate Host against an allowlist before using it in cookies or response headers.",
        )

    if reflected_body_dangerous:
        return (
            "Possible Host header injection",
            "Medium",
            "The injected Host value appeared in a successful response body in a security-relevant location, such as an absolute URL, canonical link, or form action.",
            "Manually inspect the context. Validate Host against an allowlist before using it in generated links or application output.",
        )

    # Safe rejection.
    if invalid.status in REJECT_STATUS_CODES:
        if only_server_footer:
            return (
                "Safe / strict Host validation",
                "Low",
                f"The invalid Host header was rejected with HTTP {invalid.status}. The fake Host appeared only in a server-generated error footer, which is not treated as Host header injection.",
                "No immediate issue observed. Continue using strict Host allowlisting.",
            )

        return (
            "Safe / strict Host validation",
            "Low",
            f"The invalid Host header was rejected with HTTP {invalid.status}. This indicates strict Host header validation or proxy-level filtering.",
            "No immediate issue observed. Continue using an explicit allowlist of permitted hostnames.",
        )

    # Redirects that do not use the fake Host.
    if invalid.status in REDIRECT_STATUS_CODES:
        if only_server_footer:
            return (
                "Redirects invalid Host",
                "Low",
                "The invalid Host request produced a redirect, but the injected Host appeared only in a server-generated HTML footer, not in the Location header.",
                "Check the Location header manually. Ensure redirects always use a configured canonical hostname.",
            )

        return (
            "Redirects invalid Host",
            "Low/Medium",
            "The invalid Host request produced a redirect. This is usually acceptable if the Location header points to a configured canonical domain.",
            "Check the Location header. Ensure redirects never use the untrusted request Host value.",
        )

    # Same content.
    if (
        baseline.status is not None
        and invalid.status == baseline.status
        and 200 <= invalid.status < 400
        and (same_hash or similarity >= similarity_threshold)
    ):
        return (
            "Weak Host validation",
            "Medium",
            "The website returned the same or very similar content for the correct Host and an arbitrary invalid Host. This indicates weak Host header validation. It does not, by itself, prove DNS rebinding or Host header injection.",
            "Configure the web server or reverse proxy to reject unknown Host headers, or redirect them to a fixed canonical hostname.",
        )

    # Same status but different content.
    if (
        baseline.status is not None
        and invalid.status == baseline.status
        and 200 <= invalid.status < 400
    ):
        if only_server_footer:
            return (
                "Different content with same status",
                "Low",
                "The invalid Host request returned a successful response, but the fake Host appeared only in server-generated footer text. No application-level Host injection was confirmed.",
                "Manually inspect the returned content and verify whether it is a default virtual host page.",
            )

        return (
            "Different content with same status",
            "Low/Medium",
            "The invalid Host request returned a successful response, but the content was not similar to the baseline. This may be a default virtual host or CDN response.",
            "Manually inspect the returned content and confirm whether it is a default page or the real application.",
        )

    if only_server_footer:
        return (
            "Different response",
            "Low",
            "The target responded differently to the invalid Host header. The fake Host appeared only in a server-generated footer, which is not treated as Host header injection.",
            "No immediate issue observed. Manually review unusual redirects or server-specific behavior.",
        )

    return (
        "Different response",
        "Low",
        "The target responded differently to the invalid Host header. No clear arbitrary Host acceptance was observed.",
        "No immediate issue observed, but manually review unusual redirects or server-specific behavior.",
    )


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def summarize(findings: List[HostHeaderFinding]) -> Dict[str, int]:
    stats: Dict[str, int] = {}
    for finding in findings:
        stats[finding.classification] = stats.get(finding.classification, 0) + 1
    return dict(sorted(stats.items(), key=lambda x: x[0]))


def write_json(path: str, findings: List[HostHeaderFinding], meta: Dict) -> None:
    output = {
        "meta": meta,
        "summary": summarize(findings),
        "findings": [asdict(f) for f in findings],
    }

    Path(path).write_text(
        json.dumps(output, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def write_csv(path: str, findings: List[HostHeaderFinding]) -> None:
    fieldnames = list(HostHeaderFinding.__annotations__.keys())

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for finding in findings:
            writer.writerow(asdict(finding))


def write_markdown(path: str, findings: List[HostHeaderFinding], meta: Dict) -> None:
    stats = summarize(findings)
    total = len(findings)

    lines = []
    lines.append("# Host Header Verification Report")
    lines.append("")
    lines.append("## Metadata")
    lines.append("")
    lines.append(f"- Tool: `{meta['tool']}`")
    lines.append(f"- Version: `{meta['version']}`")
    lines.append(f"- Run date: `{meta['run_date']}`")
    lines.append(f"- Fake Host header: `{meta['fake_host']}`")
    lines.append(f"- Total tests: `{total}`")
    lines.append(f"- Schemes: `{', '.join(meta['schemes'])}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Classification | Count | Percentage |")
    lines.append("|---|---:|---:|")

    for key, count in stats.items():
        pct = round((count / total) * 100, 2) if total else 0
        lines.append(f"| {key} | {count} | {pct}% |")

    lines.append("")
    lines.append("## Interpretation guide")
    lines.append("")
    lines.append("| Classification | Meaning |")
    lines.append("|---|---|")
    lines.append("| Safe / strict Host validation | Invalid Host was rejected or blocked. |")
    lines.append("| Weak Host validation | Same/similar content returned for arbitrary Host. This is a weak validation signal, not proof of exploitability. |")
    lines.append("| Possible Host header injection | Injected Host appeared in Location, Set-Cookie, or security-relevant application output. Manual verification required. |")
    lines.append("| Redirects invalid Host | Invalid Host caused redirect, but not to the injected Host. Usually safe if canonical. |")
    lines.append("| Different response | The server behaved differently; no clear arbitrary Host acceptance. |")
    lines.append("| Inconclusive | Network, timeout, or baseline failure. |")
    lines.append("")
    lines.append("## Detailed results")
    lines.append("")
    lines.append("| Target | Scheme | Baseline | Invalid Host | Similarity | Reflection | Server-footer only | Classification | Risk |")
    lines.append("|---|---|---:|---:|---:|---|---|---|---|")

    for f in findings:
        reflection = []
        if f.fake_host_reflected_in_location:
            reflection.append("Location")
        if f.fake_host_reflected_in_cookie:
            reflection.append("Cookie")
        if f.fake_host_reflected_in_headers:
            reflection.append("Headers")
        if f.fake_host_reflected_in_body:
            reflection.append("Body")

        reflection_text = ", ".join(reflection) if reflection else "No"

        lines.append(
            f"| `{f.target}` | `{f.scheme}` | "
            f"{f.baseline_status} | {f.invalid_status} | "
            f"{f.content_similarity} | {reflection_text} | "
            f"{f.fake_host_reflection_only_server_footer} | "
            f"{f.classification} | {f.risk_level} |"
        )

    Path(path).write_text("\n".join(lines), encoding="utf-8")


def write_html(path: str, findings: List[HostHeaderFinding], meta: Dict) -> None:
    stats = summarize(findings)
    total = len(findings)

    def esc(x) -> str:
        return html.escape(str(x))

    summary_rows = ""
    for key, count in stats.items():
        pct = round((count / total) * 100, 2) if total else 0
        summary_rows += f"<tr><td>{esc(key)}</td><td>{count}</td><td>{pct}%</td></tr>\n"

    result_rows = ""
    for f in findings:
        reflection = []
        if f.fake_host_reflected_in_location:
            reflection.append("Location")
        if f.fake_host_reflected_in_cookie:
            reflection.append("Cookie")
        if f.fake_host_reflected_in_headers:
            reflection.append("Headers")
        if f.fake_host_reflected_in_body:
            reflection.append("Body")

        reflection_text = ", ".join(reflection) if reflection else "No"

        result_rows += f"""
        <tr>
          <td>{esc(f.target)}</td>
          <td>{esc(f.scheme)}</td>
          <td>{esc(f.baseline_status)}</td>
          <td>{esc(f.invalid_status)}</td>
          <td>{esc(f.content_similarity)}</td>
          <td>{esc(reflection_text)}</td>
          <td>{esc(f.fake_host_reflection_only_server_footer)}</td>
          <td>{esc(f.classification)}</td>
          <td>{esc(f.risk_level)}</td>
          <td>{esc(f.interpretation)}</td>
        </tr>
        """

    doc = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Host Header Verification Report</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 30px;
      line-height: 1.45;
      color: #222;
    }}
    h1, h2 {{
      color: #111;
    }}
    table {{
      border-collapse: collapse;
      width: 100%;
      margin-bottom: 28px;
      font-size: 14px;
    }}
    th, td {{
      border: 1px solid #ccc;
      padding: 8px;
      vertical-align: top;
    }}
    th {{
      background: #f2f2f2;
    }}
    code {{
      background: #f5f5f5;
      padding: 2px 4px;
      border-radius: 3px;
    }}
    .note {{
      background: #fff8dc;
      border: 1px solid #e6d98a;
      padding: 12px;
      margin-bottom: 20px;
    }}
  </style>
</head>
<body>
  <h1>Host Header Verification Report</h1>

  <div class="note">
    <strong>Scope:</strong>
    This report is based on non-invasive GET requests comparing the correct Host header with an arbitrary invalid Host header.
    Results classified as weak validation or possible injection require manual interpretation.
  </div>

  <h2>Metadata</h2>
  <ul>
    <li>Tool: <code>{esc(meta['tool'])}</code></li>
    <li>Version: <code>{esc(meta['version'])}</code></li>
    <li>Run date: <code>{esc(meta['run_date'])}</code></li>
    <li>Fake Host header: <code>{esc(meta['fake_host'])}</code></li>
    <li>Total tests: <code>{total}</code></li>
    <li>Schemes: <code>{esc(", ".join(meta['schemes']))}</code></li>
  </ul>

  <h2>Summary</h2>
  <table>
    <thead>
      <tr>
        <th>Classification</th>
        <th>Count</th>
        <th>Percentage</th>
      </tr>
    </thead>
    <tbody>
      {summary_rows}
    </tbody>
  </table>

  <h2>Interpretation guide</h2>
  <table>
    <thead>
      <tr>
        <th>Classification</th>
        <th>Meaning</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Safe / strict Host validation</td><td>Invalid Host was rejected or blocked.</td></tr>
      <tr><td>Weak Host validation</td><td>Same or similar content returned for arbitrary Host. This is a weak validation signal, not proof of exploitability.</td></tr>
      <tr><td>Possible Host header injection</td><td>Injected Host appeared in Location, Set-Cookie, or security-relevant application output. Manual verification required.</td></tr>
      <tr><td>Redirects invalid Host</td><td>Invalid Host caused redirect, but not to the injected Host. Usually safe if canonical.</td></tr>
      <tr><td>Different response</td><td>The server behaved differently; no clear arbitrary Host acceptance.</td></tr>
      <tr><td>Inconclusive</td><td>Network, timeout, or baseline failure.</td></tr>
    </tbody>
  </table>

  <h2>Detailed results</h2>
  <table>
    <thead>
      <tr>
        <th>Target</th>
        <th>Scheme</th>
        <th>Baseline status</th>
        <th>Invalid Host status</th>
        <th>Similarity</th>
        <th>Reflection</th>
        <th>Server-footer only</th>
        <th>Classification</th>
        <th>Risk</th>
        <th>Interpretation</th>
      </tr>
    </thead>
    <tbody>
      {result_rows}
    </tbody>
  </table>
</body>
</html>
"""

    Path(path).write_text(doc, encoding="utf-8")


# ---------------------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------------------

async def run(args) -> List[HostHeaderFinding]:
    if args.domain:
        targets = [args.domain]
    elif args.url:
        targets = [args.url]
    elif args.input:
        targets = load_targets_from_file(args.input, args.tld, args.limit)
    else:
        print("No target specified. Use --domain, --url, or --input.", file=sys.stderr)
        sys.exit(1)

    if not targets:
        print("No targets found.", file=sys.stderr)
        sys.exit(1)

    schemes = [s.strip().lower() for s in args.schemes.split(",") if s.strip()]
    schemes = [s for s in schemes if s in {"http", "https"}]

    if not schemes:
        print("Invalid --schemes value. Use http, https, or https,http.", file=sys.stderr)
        sys.exit(1)

    total_tests = len(targets) * len(schemes)

    print(f"Loaded targets: {len(targets)}")
    print(f"Schemes: {', '.join(schemes)}")
    print(f"Fake Host: {args.fake_host}")
    print(f"Concurrency: {args.concurrency}; timeout: {args.timeout}s; rate: {args.rate}s")

    connector = aiohttp.TCPConnector(
        limit=args.concurrency,
        ttl_dns_cache=300,
        ssl=False,
    )

    semaphore = asyncio.Semaphore(args.concurrency)
    all_findings: List[HostHeaderFinding] = []

    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [
            test_target(
                semaphore=semaphore,
                session=session,
                target=target,
                fake_host=args.fake_host,
                schemes=schemes,
                timeout=args.timeout,
                user_agent=args.user_agent,
                body_limit=args.body_limit,
                similarity_threshold=args.similarity_threshold,
                probe_gap=args.probe_gap,
            )
            for target in targets
        ]

        completed_tests = 0

        for task in asyncio.as_completed(tasks):
            findings = await task
            all_findings.extend(findings)

            for finding in findings:
                completed_tests += 1
                print(
                    f"[{completed_tests:4d}/{total_tests}] "
                    f"{str(finding.invalid_status):>4} "
                    f"{finding.classification:<35} "
                    f"{finding.tested_url}"
                )

            if args.rate > 0:
                await asyncio.sleep(args.rate)

    return all_findings


def parse_args():
    parser = argparse.ArgumentParser(
        description="General-purpose Host header validation tester with report generation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:

  Test one domain:
    python host_header_research_tool_v2.py --domain coop.ee

  Test one URL:
    python host_header_research_tool_v2.py --url https://example.ee/login

  Test Estonian websites from Tranco:
    python host_header_research_tool_v2.py --input top-1m.csv --tld .ee --limit 100

  Test both HTTPS and HTTP:
    python host_header_research_tool_v2.py --input top-1m.csv --tld .ee --schemes https,http

  Custom output names:
    python host_header_research_tool_v2.py --input domains.txt --csv results.csv --report-html report.html
        """
    )

    target_group = parser.add_mutually_exclusive_group(required=True)
    target_group.add_argument("--domain", help="Single domain to test, e.g. coop.ee")
    target_group.add_argument("--url", help="Single full URL to test, e.g. https://example.ee/login")
    target_group.add_argument("--input", help="Input file: Tranco CSV or plain text domain/URL list")

    parser.add_argument("--tld", help="Filter input file by TLD, e.g. .ee, .fi, .de")
    parser.add_argument("--limit", type=int, help="Limit number of targets from input file")

    parser.add_argument(
        "--schemes",
        default="https",
        help="Comma-separated schemes to test: https, http, or https,http. Default: https",
    )

    parser.add_argument(
        "--fake-host",
        default=DEFAULT_FAKE_HOST,
        help=f"Fake Host header value. Default: {DEFAULT_FAKE_HOST}",
    )

    parser.add_argument(
        "--concurrency",
        type=int,
        default=DEFAULT_CONCURRENCY,
        help=f"Concurrent targets. Default: {DEFAULT_CONCURRENCY}",
    )

    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f"Request timeout in seconds. Default: {DEFAULT_TIMEOUT}",
    )

    parser.add_argument(
        "--rate",
        type=float,
        default=0.0,
        help="Delay after each completed target. Default: 0.0",
    )

    parser.add_argument(
        "--probe-gap",
        type=float,
        default=0.2,
        help="Delay between baseline and invalid Host probe. Default: 0.2",
    )

    parser.add_argument(
        "--body-limit",
        type=int,
        default=DEFAULT_BODY_LIMIT,
        help=f"Maximum bytes read from response body. Default: {DEFAULT_BODY_LIMIT}",
    )

    parser.add_argument(
        "--similarity-threshold",
        type=float,
        default=DEFAULT_SIMILARITY_THRESHOLD,
        help=f"Similarity threshold for weak Host validation. Default: {DEFAULT_SIMILARITY_THRESHOLD}",
    )

    parser.add_argument(
        "--user-agent",
        default=DEFAULT_USER_AGENT,
        help="Custom User-Agent string",
    )

    parser.add_argument(
        "--json",
        default="host_header_results_v2.json",
        help="JSON output path. Default: host_header_results_v2.json",
    )

    parser.add_argument(
        "--csv",
        default="host_header_results_v2.csv",
        help="CSV output path. Default: host_header_results_v2.csv",
    )

    parser.add_argument(
        "--report-md",
        default="host_header_report_v2.md",
        help="Markdown report output path. Default: host_header_report_v2.md",
    )

    parser.add_argument(
        "--report-html",
        default="host_header_report_v2.html",
        help="HTML report output path. Default: host_header_report_v2.html",
    )

    return parser.parse_args()


def main():
    args = parse_args()
    start = time.time()

    findings = asyncio.run(run(args))

    meta = {
        "tool": "Host Header Research Tool",
        "version": "2.0",
        "run_date": now_utc(),
        "fake_host": args.fake_host,
        "schemes": [s.strip().lower() for s in args.schemes.split(",") if s.strip()],
        "total_findings": len(findings),
        "ethical_scope": "Non-invasive GET requests only. No authentication, password reset, cache poisoning, or destructive testing.",
        "classification_note": (
            "Apache/Nginx server-generated footer reflection is not treated as Host header injection "
            "unless the fake Host appears in Location, Set-Cookie, or security-relevant application output."
        ),
    }

    write_json(args.json, findings, meta)
    write_csv(args.csv, findings)
    write_markdown(args.report_md, findings, meta)
    write_html(args.report_html, findings, meta)

    elapsed = round(time.time() - start, 2)

    print("")
    print("=" * 70)
    print("SCAN COMPLETE")
    print("=" * 70)
    print(f"Total tests       : {len(findings)}")
    print(f"JSON output       : {args.json}")
    print(f"CSV output        : {args.csv}")
    print(f"Markdown report   : {args.report_md}")
    print(f"HTML report       : {args.report_html}")
    print(f"Runtime           : {elapsed}s")
    print("=" * 70)


if __name__ == "__main__":
    main()