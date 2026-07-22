"""
======================================================================
EZENOX v1.3.0

Professional HTML Report

Responsibilities
----------------
• Generate executive HTML report
• Group findings by service
• Display vulnerability summary

Author : Ezeduties
======================================================================
"""

import os
from datetime import datetime

from reports.report_builder import ReportBuilder


class HTMLReport:

    def __init__(self):

        self.output_dir = "reports/scan_reports"

        os.makedirs(
            self.output_dir,
            exist_ok=True
        )

        self.timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        self.builder = ReportBuilder()

    def save(self, findings):

        report = self.builder.build(findings)

        filename = os.path.join(
            self.output_dir,
            f"findings_{self.timestamp}.html"
        )

        html = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="utf-8">

<title>EZENOX Report</title>

<style>

body {{
    font-family: Arial;
    background: #f4f4f4;
    margin:40px;
}}

.card {{
    background:white;
    padding:20px;
    margin-bottom:25px;
    border-radius:8px;
    box-shadow:0 2px 5px rgba(0,0,0,.15);
}}

table {{
    width:100%;
    border-collapse:collapse;
}}

th, td {{
    border:1px solid #ddd;
    padding:8px;
}}

th {{
    background:#222;
    color:white;
}}

.critical {{
    color:#d80000;
    font-weight:bold;
}}

.high {{
    color:#ff6600;
    font-weight:bold;
}}

.medium {{
    color:#cc9900;
    font-weight:bold;
}}

.low {{
    color:green;
    font-weight:bold;
}}

.unknown {{
    color:gray;
}}

</style>

</head>

<body>

<div class="card">

<h1>EZENOX Professional Vulnerability Report</h1>

<h3>Target: {report["host"]}</h3>

<table>

<tr>
<th>Total Services</th>
<th>Total Findings</th>
<th>Critical</th>
<th>High</th>
<th>Medium</th>
<th>Low</th>
</tr>

<tr>
<td>{report["summary"]["services"]}</td>
<td>{report["summary"]["findings"]}</td>
<td>{report["summary"]["critical"]}</td>
<td>{report["summary"]["high"]}</td>
<td>{report["summary"]["medium"]}</td>
<td>{report["summary"]["low"]}</td>
</tr>

</table>

</div>
"""

        for service in report["services"]:

            html += f"""

<div class="card">

<h2>Port {service['port']} / {service['service'].upper()}</h2>

<p>

<b>Vendor:</b> {service['vendor']}<br>

<b>Product:</b> {service['product']}<br>

<b>Version:</b> {service['version']}<br>

<b>Confidence:</b> {service['confidence']}<br>

<b>CPE:</b> {service['cpe']}

</p>

<table>

<tr>

<th>CVE</th>

<th>Severity</th>

<th>Description</th>

</tr>
"""

            for vuln in service["vulnerabilities"]:

                severity = vuln["severity"].lower()

                html += f"""

<tr>

<td>{vuln['cve']}</td>

<td class="{severity}">{vuln['severity']}</td>

<td>{vuln['description']}</td>

</tr>
"""

            html += """

</table>

</div>
"""

        html += """

</body>

</html>
"""

        with open(filename, "w", encoding="utf-8") as file:

            file.write(html)

        print(f"[+] HTML Report: {filename}")
