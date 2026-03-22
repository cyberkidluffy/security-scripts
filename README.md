# Security Automation Scripts

Python security scripts built as part of my 2026 cybersecurity upskilling journey.

## Scripts

### 1. Log Parser (`log_parser.py`)
Reads a log file and automatically flags suspicious events containing keywords like FAILED, ERROR, UNAUTHORIZED and DENIED.

**Use case:** Automate manual log review in SOC environments.

**Usage:**
```python
python log_parser.py
```

### 2. IP Reputation Checker (`ip_checker.py`)
Queries the AbuseIPDB threat intelligence API to check if an IP address has been reported for malicious activity. Returns abuse score, country, and total reports.

**Use case:** Automate IP triage during incident response and alert investigation.

**Usage:**
```python
python ip_checker.py
```

## Tools & APIs
- Python 3.14
- AbuseIPDB API (abuseipdb.com)
