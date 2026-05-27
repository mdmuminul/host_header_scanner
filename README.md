# Host Header Verification Scanner

This repository contains a research-oriented scanner for testing how websites validate the HTTP `Host` header.

The project was developed for the research topic:

**Verification of the Host Header by Estonian Websites**

The scanner compares a normal request using the correct Host header with a second request using an invalid Host header. It then classifies the result based on whether the website rejects the invalid Host, returns the same content, redirects, or reflects the injected Host value in security-relevant places.

---

## Purpose of the Project

Modern websites often use the HTTP `Host` header for routing requests through web servers, reverse proxies, load balancers, and CDNs. If a website accepts arbitrary Host values, it may indicate weak Host validation.

This scanner helps identify:

- websites with strict Host validation,
- websites with weak Host validation,
- DNS-rebinding-relevant candidates,
- possible Host header injection indicators,
- redirects and other non-confirming behavior.

The tool is designed for academic and defensive research. It does **not** exploit websites.

---

## What the Scanner Tests

For each target website, the scanner sends two requests.

Normal baseline request:

```http
GET / HTTP/1.1
Host: real-domain.ee

Invalid Host request:

GET / HTTP/1.1
Host: invalid-host-test.example

Then it compares the responses using:

HTTP status code,
response body similarity,
normalized response hash,
Location header,
Set-Cookie header,
Host reflection in headers or body,
server-generated footer reflection,
final classification.
Repository Structure

Recommended structure:

.
├── host_header_research_tool_v2.py
├── analyze_host_header_results.py
├── top-1m.csv
├── results/
│   ├── estonian_host_header_results_v2.csv
│   ├── estonian_host_header_results_v2.json
│   ├── estonian_host_header_report_v2.md
│   └── estonian_host_header_report_v2.html
├── research/
│   ├── estonian_research_analysis_summary.csv
│   ├── estonian_research_dns_rebinding_candidates.csv
│   ├── estonian_research_failed_host_validation.csv
│   ├── estonian_research_possible_host_injection.csv
│   └── estonian_research_grouped_results.html
└── README.md
Requirements

Python 3.9 or newer is recommended.

Install the required dependency:

pip install aiohttp
How to Run the Scanner
1. Test a single domain
python host_header_research_tool_v2.py \
  --domain example.ee \
  --schemes https,http

This tests both HTTPS and HTTP for one domain.

2. Test only HTTP
python host_header_research_tool_v2.py \
  --domain example.ee \
  --schemes http

HTTP results are more relevant for DNS rebinding analysis.

3. Test only HTTPS
python host_header_research_tool_v2.py \
  --domain example.ee \
  --schemes https

HTTPS results are useful for Host validation and possible Host header injection analysis, but HTTPS weak validation alone is not direct DNS rebinding proof.

4. Test domains from a file

The input file can be a plain text file with one domain per line:

example.ee
test.ee
site.ee

Run:

python host_header_research_tool_v2.py \
  --input domains.txt \
  --schemes https,http
5. Test .ee domains from the Tranco Top 1M list

If you have a Tranco CSV file such as top-1m.csv, run:

python host_header_research_tool_v2.py \
  --input top-1m.csv \
  --tld .ee \
  --schemes https,http \
  --concurrency 5 \
  --timeout 10 \
  --rate 0.2 \
  --csv estonian_host_header_results_v2.csv \
  --json estonian_host_header_results_v2.json \
  --report-md estonian_host_header_report_v2.md \
  --report-html estonian_host_header_report_v2.html

This command:

loads domains from top-1m.csv,
keeps only .ee domains,
tests both HTTPS and HTTP,
saves CSV, JSON, Markdown, and HTML reports.
Command Options
Option	Meaning
--domain	Test one domain, for example example.ee.
--url	Test one full URL.
--input	Test domains from a file or Tranco CSV.
--tld	Filter input domains by TLD, for example .ee.
--schemes	Choose http, https, or https,http.
--fake-host	Custom invalid Host value. Default: invalid-host-test.example.
--concurrency	Number of targets tested at the same time.
--timeout	Maximum time to wait for a response.
--rate	Delay between completed target batches.
--csv	CSV output file path.
--json	JSON output file path.
--report-md	Markdown report output path.
--report-html	HTML report output path.
What Concurrency, Timeout, and Rate Mean

Concurrency means how many websites the tool tests at the same time.

Timeout means how long the tool waits for a website to respond before giving up.

Rate means a small waiting time between tests so the scanner does not send requests too aggressively.

Example:

--concurrency 5 --timeout 10 --rate 0.2

This means the tool tests up to 5 targets at the same time, waits up to 10 seconds for each request, and pauses briefly between completed batches.

Scanner Classifications
Classification	Meaning
Safe / strict Host validation	Invalid Host was rejected or blocked.
Weak Host validation	Same or highly similar content was returned for correct and invalid Host.
Possible Host header injection	Fake Host appeared in Location, Set-Cookie, or security-relevant output.
Redirects invalid Host	Invalid Host caused a redirect, but not necessarily unsafe.
Different response	Invalid Host response was different from baseline.
Different content with same status	Same HTTP status, but different content.
Inconclusive	Timeout, network error, or unreliable result.
Research-Level Interpretation

For the final research report, the scanner results can be grouped like this:

Research Category	Scanner Classification
Strict Host validation	Safe / strict Host validation
Failed Host validation	Weak Host validation
DNS-rebinding-relevant candidate	HTTP + Weak Host validation
Possible Host header injection indicator	Possible Host header injection
Other / non-confirming behavior	Redirects invalid Host, Different response, Different content with same status
Inconclusive	Inconclusive
Important Interpretation Notes
Weak Host Validation

A website is classified as Weak Host validation when the invalid Host request returns the same or highly similar content as the normal request.

This means the website failed the Host validation check used in this research.

However, it does not automatically prove:

DNS rebinding exploitation,
Host header injection,
password reset poisoning,
cache poisoning.

For DNS rebinding, the most relevant case is:

HTTP + Weak Host validation
Possible Host Header Injection Indicator

A website is classified as Possible Host header injection when the injected Host appears in a security-relevant response location, such as:

Location header,
Set-Cookie header,
generated body output.

Example:

Location: https://invalid-host-test.example/

This is an indicator only. It requires manual verification before it can be treated as a confirmed vulnerability.

Running the Analyzer

The analyzer script reads the scanner CSV output and creates research-focused result files.

Run:

python analyze_host_header_results.py \
  --input estonian_host_header_results_v2.csv \
  --prefix estonian_research

This generates:

estonian_research_analysis_summary.csv
estonian_research_dns_rebinding_candidates.csv
estonian_research_failed_host_validation.csv
estonian_research_possible_host_injection.csv
estonian_research_grouped_results.md
estonian_research_grouped_results.html
Example Scanner Output

Example terminal output:

Loaded targets: 675
Schemes: https, http
Fake Host: invalid-host-test.example
Concurrency: 5; timeout: 10s; rate: 0.2s

[   1/1350]  403 Safe / strict Host validation      https://example.ee/
[   2/1350]  200 Weak Host validation               http://example.ee/
[   3/1350]  301 Possible Host header injection     http://example2.ee/
