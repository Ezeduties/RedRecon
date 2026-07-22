from discovery.port_scanner import Scanner
from core.scanner import CoreScanner

scanner = Scanner()

scan = scanner.scan_host("10.0.9.5")

core = CoreScanner()

findings = core.analyze_host(scan)

print()

print("=" * 70)
print(f"Total Findings : {len(findings)}")
print("=" * 70)

for finding in findings[:10]:

    print()

    print(f"{finding.service.upper()}")

    print(f"{finding.product} {finding.version}")

    print(f"{finding.cve}")

    print(f"{finding.severity}")
