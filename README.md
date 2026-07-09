RedRecon

Professional Network Reconnaissance Framework written in Python

⸻

Overview

RedRecon is a modular Python-based network reconnaissance framework developed as part of my cybersecurity learning journey toward becoming a Penetration Tester and Red Team Operator.

The goal of RedRecon is not only to scan networks, but to grow into a complete reconnaissance and vulnerability assessment framework comparable in design to professional security tools.

⸻

Current Features

Host Validation
Port Scanning
Service Detection
Operating System Detection
Version Detection
Error Handling
CSV Report Generation
JSON Report Generation
TXT Report Generation
Modular Python Architecture

⸻

Technologies

Python 3
Nmap
python-nmap
Scapy
Rich
Colorama
Requests

⸻

Project Structure

RedRecon/

├── banner.py
├── redrecon.py
├── scanner.py
├── validator.py
├── reports.py
├── utils.py
├── install.sh
├── requirements.txt
├── README.md
├── tests/
│   ├── test_scanner.py
│   ├── test_reports.py
│   └── test_validator.py
├── reports/
└── venv/

⸻

Installation

Clone the repository:

git clone git@github.com:Ezeduties/RedRecon.git

cd RedRecon

⸻

Run the installer:

chmod +x install.sh

./install.sh

⸻

Activate the virtual environment:

source venv/bin/activate

⸻

Start RedRecon:

python3 redrecon.py

⸻ 

Example Output

Host      : 10.0.9.5

Hostname  : Metasploitable2

State     : up

Operating System

Linux 2.6.x

Open Ports

21 FTP
22 SSH
80 HTTP
3306 MySQL

⸻

Development Roadmap

Version 1.0

Host Validation
Network Scanning
Service Enumeration
OS Detection
Reporting Engine

Version 1.1

Vulnerability Assessment
CVE Matching
Risk Scoring

Version 1.2

DNS Enumeration
SMB Enumeration
HTTP Enumeration
SSH Enumeration

Version 2.0

Plugin Framework
HTML Reports
PDF Reports
Configuration Profiles

⸻

Disclaimer

RedRecon is intended for educational purposes and authorized security assessments only.

Always obtain permission before scanning networks you do not own or have explicit authorization to test.

⸻

Author

Emmanuel Eze

Cybersecurity Student

Institute of Cybersecurity Professionals

GitHub:
https://github.com/Ezeduties
