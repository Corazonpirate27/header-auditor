# HTTP Security Header Auditor

A security tool that checks websites for missing HTTP security headers.

## What it does
- Checks 6 critical security headers
- Shows which headers are missing
- Displays vulnerability risk for each missing header
- Beautiful terminal table output

## Headers checked
- X-Frame-Options (Clickjacking protection)
- X-Content-Type-Options (MIME sniffing protection)
- Content-Security-Policy (XSS protection)
- Strict-Transport-Security (HTTPS enforcement)
- Referrer-Policy (Data leakage prevention)
- Permissions-Policy (Hardware access control)

## Tools used
- Python 3.12
- requests
- Rich (terminal formatting)

## How to run
pip install requests rich
python auditor.py

## Real world test results
- google.com    → 1/6 headers found
- facebook.com  → 5/6 headers found


## Author
Corazonpirate27
