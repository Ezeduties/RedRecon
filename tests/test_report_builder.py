from discovery.port_scanner import Scanner

from core.scanner import CoreScanner

from reports.report_builder import ReportBuilder


scanner = Scanner()

scan = scanner.scan_host("10.0.9.5")

core = CoreScanner()

findings = core.analyze_host(scan)

builder = ReportBuilder()

report = builder.build(findings)

print()

print("=" * 70)

print("SUMMARY")

print("=" * 70)

print(report["summary"])

print()

print("=" * 70)

print("FIRST SERVICE")

print("=" * 70)

print(report["services"][0])
