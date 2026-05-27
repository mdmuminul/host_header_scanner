# Host Header Verification Scanner

This repository contains a Python-based scanner for testing how websites handle the HTTP `Host` header. It compares a normal request using the correct Host header with a second request using an invalid Host header, then classifies the website's behavior.

The tool is intended for academic, defensive, and non-invasive web security research.

---

## What the Scanner Does

For each target website, the scanner sends two requests.

Normal request:

```http
GET / HTTP/1.1
Host: real-domain.com
```

Invalid Host request:

```http
GET / HTTP/1.1
Host: invalid-host-test.example
```

The scanner compares both responses and checks:

- HTTP status codes
- response body similarity
- normalized response hash
- redirect `Location` header
- `Set-Cookie` header
- reflection of the injected Host value
- whether reflection appears only in a default server footer
- final classification

---

## Main Use Cases

This scanner can help identify:

- websites with strict Host header validation
- websites with weak Host header validation
- HTTP endpoints relevant to DNS rebinding analysis
- possible Host header injection indicators
- redirect behavior caused by invalid Host headers
- inconclusive or misconfigured responses

The scanner does not confirm full exploitation. It only identifies observable indicators.

---

## Requirements

Python 3.9 or newer is recommended.

Install the required dependency:

```bash
pip install aiohttp
```

---

## Repository Structure

Recommended structure:

```text
.
├── host_header_research_tool_v2.py
├── analyze_host_header_results.py
├── top-1m.csv
├── results/
│   ├── estonian_host_header_results_v2.csv
│   ├── estonian_host_header_results_v2.json
│   ├── estonian_host_header_report_v2.md
│   └── estonian_host_header_report_v2.html
└── README.md
```

---

## How to Run the Scanner

### Test a single domain

```bash
python host_header_research_tool_v2.py \
  --domain example.ee \
  --schemes https,http
```

This tests both HTTPS and HTTP for one domain.

---

### Test only HTTP

```bash
python host_header_research_tool_v2.py \
  --domain example.ee \
  --schemes http
```

HTTP findings are especially useful when discussing DNS rebinding relevance.

---

### Test only HTTPS

```bash
python host_header_research_tool_v2.py \
  --domain example.ee \
  --schemes https
```

HTTPS findings are useful for Host validation and possible Host header injection analysis.

---

### Test a full URL

```bash
python host_header_research_tool_v2.py \
  --url https://example.ee/login \
  --schemes https
```

---

### Test domains from a text file

Create a file named `domains.txt`:

```text
example.ee
test.ee
site.ee
```

Run:

```bash
python host_header_research_tool_v2.py \
  --input domains.txt \
  --schemes https,http
```

---

### Test `.ee` domains from Tranco Top 1M

If you have a Tranco CSV file such as `top-1m.csv`, run:

```bash
python host_header_research_tool_v2.py \
  --input top-1m.csv \
  --tld .ee \
  --schemes https,http \
  --concurrency 5 \
  --timeout 10 \
  --rate 0.2 \
  --csv results/estonian_host_header_results_v2.csv \
  --json results/estonian_host_header_results_v2.json \
  --report-md results/estonian_host_header_report_v2.md \
  --report-html results/estonian_host_header_report_v2.html
```

This command:

- loads domains from `top-1m.csv`
- filters only `.ee` domains
- tests both HTTPS and HTTP
- saves CSV, JSON, Markdown, and HTML reports

---

## Important Parameters

| Parameter | Description |
|---|---|
| `--domain` | Test one domain, for example `example.ee`. |
| `--url` | Test one full URL. |
| `--input` | Test domains from a file or Tranco CSV. |
| `--tld` | Filter input domains by TLD, for example `.ee`. |
| `--schemes` | Choose `http`, `https`, or `https,http`. |
| `--fake-host` | Invalid Host value used for testing. Default: `invalid-host-test.example`. |
| `--concurrency` | Number of targets tested at the same time. |
| `--timeout` | Maximum time to wait for a response. |
| `--rate` | Delay between completed target batches. |
| `--csv` | Path for CSV output. |
| `--json` | Path for JSON output. |
| `--report-md` | Path for Markdown report output. |
| `--report-html` | Path for HTML report output. |

---

## Recommended Scan Settings

For a careful scan:

```bash
--concurrency 2 --timeout 10 --rate 0.5
```

For a faster scan:

```bash
--concurrency 5 --timeout 10 --rate 0.2
```

`concurrency` controls how many targets are tested at the same time.  
`timeout` controls how long the scanner waits for a response.  
`rate` adds a small pause between completed tests.

---

## Scanner Classifications

| Classification | Meaning |
|---|---|
| `Safe / strict Host validation` | Invalid Host was rejected or blocked. |
| `Weak Host validation` | Same or highly similar content was returned for correct and invalid Host. |
| `Possible Host header injection` | Fake Host appeared in `Location`, `Set-Cookie`, or security-relevant output. |
| `Redirects invalid Host` | Invalid Host caused a redirect, but not necessarily unsafe. |
| `Different response` | Invalid Host response was different from the baseline. |
| `Different content with same status` | Same HTTP status, but different page content. |
| `Inconclusive` | Timeout, network error, or unreliable result. |

---

## How to Interpret Results

### Weak Host Validation

A website is classified as `Weak Host validation` when the invalid Host request returns the same or highly similar content as the normal request.

This means the website failed the Host validation check used by this scanner. However, it does not automatically prove DNS rebinding or Host header injection.

For DNS rebinding discussion, the most relevant case is:

```text
HTTP + Weak Host validation
```

---

### Possible Host Header Injection

A website is classified as `Possible Host header injection` when the fake Host appears in a security-relevant response location, such as:

- `Location` header
- `Set-Cookie` header
- generated body output

Example:

```http
Location: https://invalid-host-test.example/
```

This is only an indicator. It requires manual verification before it can be treated as a confirmed vulnerability.

---

## Running the Analyzer

The analyzer script groups scanner results into research-level categories.

Run:

```bash
python analyze_host_header_results.py \
  --input results/estonian_host_header_results_v2.csv \
  --prefix results/estonian_research
```

This generates:

```text
estonian_research_analysis_summary.csv
estonian_research_dns_rebinding_candidates.csv
estonian_research_failed_host_validation.csv
estonian_research_possible_host_injection.csv
estonian_research_grouped_results.md
estonian_research_grouped_results.html
```

---

## Manual Verification Example

You can manually check a finding with `curl`.

Baseline request:

```bash
curl -s -i http://example.ee/ -H "Host: example.ee"
```

Invalid Host request:

```bash
curl -s -i http://example.ee/ -H "Host: invalid-host-test.example"
```

If both responses are the same or highly similar, the website may have weak Host validation.

The options mean:

- `-s` hides curl’s progress output
- `-i` includes response headers

---

## Ethical Scope

This tool is designed for non-invasive testing.

The scanner does:

- send GET requests
- compare responses
- check headers and body content
- generate reports

The scanner does not:

- log in
- submit forms
- trigger password reset flows
- test cache poisoning
- execute JavaScript
- perform real DNS rebinding
- send destructive requests
- exploit vulnerabilities

Only test systems where you have permission or where testing is allowed.

---

## Limitations

The scanner results should be interpreted carefully.

Main limitations:

- only public websites are tested
- only unauthenticated GET requests are sent
- password reset flows are not tested
- cache poisoning is not tested
- real DNS rebinding is not executed in a browser
- HTTPS certificate constraints are not bypassed
- CDNs, WAFs, reverse proxies, redirects, and default hosting pages may affect results

---

## Recommended Wording

Use careful wording when reporting results.

Use:

```text
Weak Host validation
```

instead of:

```text
DNS rebinding vulnerable
```

Use:

```text
Possible Host header injection indicator
```

instead of:

```text
Confirmed Host header injection vulnerability
```

The scanner identifies Host header handling behavior and risk indicators, not confirmed exploitation.

---

## License

This project is intended for academic and defensive security research. Use responsibly.
