from core.scanner import CoreScanner

scanner = CoreScanner()

services = [

    (21, "ftp"),

    (22, "ssh"),

    (25, "smtp"),

    (80, "http")

]

for port, service in services:

    print("=" * 70)

    print(f"{service.upper()} ({port})")

    findings = scanner.analyze_service(

        "10.0.9.5",

        port,

        service

    )

    if findings:

        for finding in findings:

            print(finding)

    else:

        print("No findings.")
