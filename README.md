# EZENOX

> Professional Network Reconnaissance & Vulnerability Assessment Framework

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Linux-success.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Version](https://img.shields.io/badge/Version-1.3.0-red.svg)

---

EZENOX is a modular Python-based Network Reconnaissance and Vulnerability Assessment Framework developed for cybersecurity professionals, penetration testers, students, and security researchers.

The framework combines network discovery, service fingerprinting, software identification, CPE generation, and vulnerability correlation using the National Vulnerability Database (NVD) into a clean, extensible architecture.

Designed with scalability in mind, EZENOX separates each component into dedicated modules, making future enhancements such as stealth scanning, DNS reconnaissance, plugin support, and OSINT integration straightforward.

---

# Features

### Reconnaissance

- TCP Port Scanning
- Service Discovery
- Banner Collection
- Protocol Identification
- Operating System Detection

### Fingerprinting

- Product Detection
- Version Detection
- Vendor Detection
- CPE 2.3 Generation
- Confidence Scoring

### Vulnerability Assessment

- NVD API Integration
- CVE Enumeration
- Severity Classification
- Structured Findings

### Reporting

- TXT Reports
- JSON Reports
- CSV Reports
- HTML Executive Reports

### User Interface

- Professional Console Interface
- Rich Terminal Colors
- Interactive Menu
- Domain or IP Target Support
- Stealth Mode Toggle (v1.4.0)

---

# Why EZENOX?

Unlike many simple Nmap wrappers, EZENOX is designed as a modular cybersecurity framework rather than a single-purpose scanner.

Its architecture separates scanning, evidence collection, fingerprinting, vulnerability analysis, and reporting into independent components, making it easier to extend and maintain as the project evolves.

---

# Installation

## System Requirements

Before installing EZENOX, ensure your system meets the following requirements:

- Linux (Kali Linux recommended)
- Python 3.11 or newer
- Nmap installed and available in your system PATH
- Git
- Internet connection (required for NVD vulnerability lookups)

---

## Clone the Repository
git clone git@github.com:Ezeduties/EZENOX.git

Enter the project directory:
cd EZENOX

---

## Create a Virtual Environment
python3 -m venv venv

Activate the virtual environment:
source venv/bin/activate

---

## Install Dependencies

Install all required Python packages:
pip install -r requirements.txt

---

## Verify Nmap Installation

EZENOX uses Nmap as its scanning engine.

Verify that Nmap is installed:
nmap --version

If installed successfully, the version information will be displayed.

---

# Quick Start

Launch EZENOX with:
python3 main.py

You should see the EZENOX banner followed by the interactive menu.
███████╗███████╗███████╗███╗   ██╗ ██████╗ ██╗  ██╗
██╔════╝╚══███╔╝██╔════╝████╗  ██║██╔═══██╗╚██╗██╔╝
█████╗    ███╔╝ █████╗  ██╔██╗ ██║██║   ██║ ╚███╔╝
██╔══╝   ███╔╝  ██╔══╝  ██║╚██╗██║██║   ██║ ██╔██╗
███████╗███████╗███████╗██║ ╚████║╚██████╔╝██╔╝ ██╗
╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝

Example menu:
1. Single Host Scan (IP or Domain)
2. Multiple Host Scan
3. Network Range Scan
4. Stealth Mode                 [State: OFF]
5. About
0. Exit

---

# First Scan

Select Single Host Scan and enter either an IP address or a domain name.

Example:
Target (IP or Domain): 10.0.9.5

or
Target (IP or Domain): scanme.nmap.org

After the scan completes, EZENOX automatically performs:

- Network discovery
- Service fingerprinting
- Vendor detection
- CPE generation
- NVD vulnerability lookup
- Executive report generation

Generated reports are saved in:
reports/scan_reports/

Supported report formats include:

- HTML
- TXT
- JSON
- CSV

---

# Usage Guide

EZENOX provides an interactive command-line interface (CLI) designed for ease of use while maintaining a professional workflow.

After launching the application:
python3 main.py

the main menu is displayed.
1. Single Host Scan (IP or Domain)
2. Multiple Host Scan
3. Network Range Scan
4. Stealth Mode                 State: OFF
5. About
0. Exit

---

# Single Host Scan

The Single Host Scan accepts either:

- IPv4 Address
- Hostname
- Domain Name

Example:
Target (IP or Domain): 10.0.9.5

or
Target (IP or Domain): scanme.nmap.org

During the scan, EZENOX performs the following stages:
Target Discovery
        │
        ▼
Port Scanning
        │
        ▼
Banner Collection
        │
        ▼
Software Fingerprinting
        │
        ▼
Vendor Detection
        │
        ▼
CPE Generation
        │
        ▼
Confidence Scoring
        │
        ▼
NVD Vulnerability Lookup
        │
        ▼
Executive Report Generation

---

# Scan Summary

After every scan, EZENOX displays an executive summary similar to the following:
======================================================================
SCAN SUMMARY
======================================================================

Target         : 10.0.9.5
Services       : 4
Findings       : 214
Critical       : 28
High           : 64
Medium         : 106
Low            : 16
Unknown        : 0

This provides a quick overview of the security posture before reviewing the detailed reports.

---

# Report Generation

EZENOX automatically generates multiple report formats after every successful scan.

| Report | Purpose |
|---------|----------|
| HTML | Executive vulnerability report |
| TXT | Human-readable console report |
| JSON | Structured data for automation |
| CSV | Spreadsheet analysis |

Reports are stored in:
reports/scan_reports/

Example:
findings_20260722_103501.html
scan_20260722_103501.txt
scan_20260722_103501.json
scan_20260722_103501.csv

---

# Current Capabilities

EZENOX v1.3.0 currently supports:

- TCP Service Discovery
- Banner Collection
- Service Fingerprinting
- Vendor Identification
- Product Version Detection
- CPE 2.3 Generation
- Confidence Scoring
- NVD CVE Lookup
- Executive Reporting

---

# Stealth Mode

Stealth Mode has been introduced into the user interface as the foundation for future reconnaissance enhancements.

Current status:
Stealth Mode    State: OFF

In EZENOX v1.3.0, this option is a user interface placeholder and does not modify scanning behavior.

A fully functional Stealth Engine is planned for v1.4.0.

---

# Supported Services

The current release includes protocol collectors for common network services:

- FTP
- SSH
- HTTP
- HTTPS
- SMTP
- POP3
- IMAP

The modular collector architecture allows additional protocols to be integrated in future releases with minimal changes to the scanning engine.

---

# Project Architecture

EZENOX follows a modular architecture where each major responsibility is isolated into its own package. This design improves maintainability, testing, and future extensibility.
EZENOX/
│
├── collectors/
│   ├── base.py
│   ├── ftp.py
│   ├── http.py
│   ├── https.py
│   ├── imap.py
│   ├── pop3.py
│   ├── smtp.py
│   └── ssh.py
│
├── core/
│   ├── dispatcher.py
│   └── scanner.py
│
├── discovery/
│   └── port_scanner.py
│
├── evidence/
│   ├── console.py
│   └── evidence.py
│
├── fingerprinting/
│   ├── banner_parser.py
│   ├── confidence.py
│   ├── cpe_generator.py
│   ├── http_parser.py
│   └── vendor.py
│
├── reports/
│   ├── html_report.py
│   ├── report_builder.py
│   ├── report_writer.py
│   ├── vulnerability_report.py
│   └── scan_reports/
│
├── ui/
│   ├── banner.py
│   └── menu.py
│
├── utils/
│   ├── helpers.py
│   └── validator.py
│
├── vulnerability/
│   ├── finding_engine.py
│   ├── findings.py
│   ├── nvd_client.py
│   └── nvd_matcher.py
│
├── tests/
├── main.py
├── version.py
├── requirements.txt
└── README.md

---

# Module Overview

## collectors/

Protocol-specific collectors responsible for communicating with network services and gathering raw evidence.

Current collectors include:

- FTP
- SSH
- HTTP
- HTTPS
- SMTP
- POP3
- IMAP

---

## core/

Coordinates the complete scanning workflow.

Responsibilities include:

- Dispatching protocol collectors
- Coordinating scans
- Running fingerprint analysis
- Executing vulnerability assessment
- Generating reports

---

## discovery/

Handles host discovery and service enumeration using the Nmap scanning engine.

Responsibilities include:

- Port discovery
- Service detection
- Operating system detection

---

## fingerprinting/

Converts collected banners and service information into structured software fingerprints.

Capabilities include:

- Product identification
- Version extraction
- Vendor detection
- CPE generation
- Confidence scoring

---

## vulnerability/

Correlates detected software with known vulnerabilities.

Components include:

- Finding model
- Finding engine
- NVD API client
- Local matcher

---

## reports/

Responsible for converting scan results into professional reports.

Supported formats:

- HTML
- TXT
- JSON
- CSV

---

## ui/

Contains the interactive console interface.

Components include:

- ASCII banner
- Interactive menu
- User prompts

---

## utils/

Shared helper functions used throughout the framework.

Examples include:

- Input validation
- Report directory creation
- Timestamp generation
- Console utilities

---

# Design Principles

EZENOX is designed around the following engineering principles:

- Modular architecture
- Separation of concerns
- Readable and maintainable code
- Extensible plugin-friendly design
- Reusable components
- Professional reporting
- Hands-on cybersecurity learning

---

# Testing

EZENOX includes a growing suite of test modules covering core functionality.

Current areas include:

- Collectors
- Dispatcher
- Fingerprinting
- Report generation
- NVD integration
- Scanner engine
- Findings
- Utility functions

As new capabilities are added, corresponding tests are included to improve reliability and reduce regressions.

---

# Roadmap

EZENOX follows an incremental release model, where each version introduces focused improvements while maintaining a stable foundation.

## v1.3.0 (Current Release)

### Reconnaissance

- TCP Port Scanning
- Service Discovery
- Operating System Detection
- Banner Collection

### Fingerprinting

- Product Detection
- Version Detection
- Vendor Detection
- CPE 2.3 Generation
- Confidence Scoring

### Vulnerability Assessment

- NVD API Integration
- CVE Enumeration
- Severity Classification

### Reporting

- HTML Reports
- TXT Reports
- JSON Reports
- CSV Reports

### User Interface

- Professional Console Banner
- Interactive Menu
- Single Host Scanning (IP & Domain)
- Stealth Mode Toggle (UI Placeholder)

---

## Planned for v1.4.0

The next release focuses on advanced reconnaissance capabilities.

Planned features include:

- Functional Stealth Mode
- SYN Stealth Scanning
- Configurable Nmap Timing Profiles
- Rich Progress Indicators
- Improved HTML Dashboard
- Enhanced Scan Summary
- Better Logging
- Additional Protocol Collectors

---

## Future Releases

Planned long-term enhancements include:

- DNS Enumeration
- Subdomain Enumeration
- WHOIS Lookup
- SSL/TLS Analysis
- Screenshot Capture (HTTP/HTTPS)
- Plugin System
- REST API
- Multi-threaded Scanning
- PDF Report Generation
- CVSS Score Visualization
- Docker Support
- CI/CD Integration

---

# Contributing

Contributions are welcome.

If you would like to improve EZENOX:

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Add or update tests where appropriate.
5. Submit a Pull Request with a clear description of the changes.

Please ensure code remains modular, readable, and well documented.

---

# License

This project is released under the MIT License.

See the LICENSE file for details.

---

# Author

Ezeduties

GitHub: https://github.com/Ezeduties

EZENOX is a personal cybersecurity project focused on practical learning, offensive security research, and building a professional-grade reconnaissance framework through iterative development.

---

# Acknowledgements

EZENOX builds upon the work of the open-source cybersecurity community.

Special thanks to the maintainers of:

- Python
- Nmap
- python-nmap
- Rich
- Requests
- The National Vulnerability Database (NVD)

---

# Disclaimer

EZENOX is intended for educational purposes, security research, and authorized security assessments only.

Users are solely responsible for ensuring they have permission before scanning or assessing any systems or networks.

Unauthorized use of this software may violate applicable laws and regulations.

---

<p align="center">

EZENOX v1.3.0

*Professional Network Reconnaissance & Vulnerability Assessment Framework*

Developed with ❤️ by Ezeduties

</p>
