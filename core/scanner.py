"""
======================================================================
EZENOX v1.3.0

Core Scanner

Responsibilities
----------------
• Perform network scan
• Collect protocol evidence
• Analyze vulnerabilities
• Generate reports
• Display scan summary

Author : Ezeduties
======================================================================
"""

from discovery.port_scanner import Scanner

from vulnerability.finding_engine import FindingEngine

from reports.report_writer import ReportGenerator
from reports.report_builder import ReportBuilder
from reports.vulnerability_report import VulnerabilityReport
from reports.html_report import HTMLReport


class CoreScanner:

    def __init__(self):

        self.scanner = Scanner()

        self.engine = FindingEngine()

        self.builder = ReportBuilder()

    # ---------------------------------------------------------

    def scan_host(self, target):

        return self.scanner.scan_host(target)

    # ---------------------------------------------------------

    def analyze_host(self, scan):

        return self.engine.analyze(scan)

    # ---------------------------------------------------------

    def run(self, target, stealth=False):

        print("=" * 70)
        print("EZENOX Professional Network Reconnaissance Framework")
        print("=" * 70)
        print()

        print(f"Target : {target}")
        
        mode = "ON" if stealth else "OFF"
        
        print(f"Stealth Mode : {mode}")
        print()

        # -----------------------------------------------------
        # Scan
        # -----------------------------------------------------

        scan = self.scan_host(target)

        # -----------------------------------------------------
        # Analyze
        # -----------------------------------------------------

        findings = self.analyze_host(scan)

        # -----------------------------------------------------
        # Build Report Structure
        # -----------------------------------------------------

        report = self.builder.build(findings)

        # -----------------------------------------------------
        # Save Scan Reports
        # -----------------------------------------------------

        ReportGenerator(scan).export_all()

        # -----------------------------------------------------
        # Save Vulnerability Reports
        # -----------------------------------------------------

        try:
            VulnerabilityReport().save(report)
        except Exception as e:
            print(f"[ERROR] Vulnerability Report: {e}")

        try:
            HTMLReport().save(findings)
        except Exception as e:
            print(f"[ERROR] HTML Report: {e}")

        # -----------------------------------------------------
        # Summary
        # -----------------------------------------------------

        summary = report["summary"]

        print()
        print("=" * 70)
        print("SCAN SUMMARY")
        print("=" * 70)

        print(f"Target         : {target}")
        print(f"Services       : {summary['services']}")
        print(f"Findings       : {summary['findings']}")
        print(f"Critical       : {summary['critical']}")
        print(f"High           : {summary['high']}")
        print(f"Medium         : {summary['medium']}")
        print(f"Low            : {summary['low']}")
        print(f"Unknown        : {summary['unknown']}")

        print()

        return findings
