from vulnerability.nvd_matcher import NVDMatcher

matcher = NVDMatcher()

samples = [

    "cpe:2.3:a:vsftpd:vsftpd:2.3.4:*:*:*:*:*:*:*",

    "cpe:2.3:a:apache:http_server:2.2.8:*:*:*:*:*:*:*",

    "cpe:2.3:a:php:php:5.2.4:*:*:*:*:*:*:*"

]

for cpe in samples:

    print("=" * 70)

    print(cpe)

    findings = matcher.match(cpe)

    if findings:

        for finding in findings:

            print(f"CVE       : {finding['cve']}")
            print(f"Severity : {finding['severity']}")
            print(f"Summary  : {finding['description']}")

    else:

        print("No matching vulnerabilities.")
