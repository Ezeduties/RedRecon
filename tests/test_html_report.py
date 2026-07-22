from discovery.port_scanner import Scanner

from core.scanner import CoreScanner

from reports.html_report import HTMLReport


scanner = Scanner()

scan = scanner.scan_host("10.0.9.5")

core = CoreScanner()

findings = core.analyze_host(scan)

report = HTMLReport()

report.save(findings)

print()

print(f"Saved {len(findings)} findings.")
