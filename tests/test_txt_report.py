from discovery.port_scanner import Scanner
from core.scanner import CoreScanner
from reports.vulnerability_report import VulnerabilityReport

scanner = Scanner()

scan = scanner.scan_host("10.0.9.5")

core = CoreScanner()

findings = core.analyze_host(scan)

report = VulnerabilityReport()

report.save(findings)

print(f"\nSaved {len(findings)} findings.")
