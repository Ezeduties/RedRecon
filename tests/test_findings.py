from vulnerability.findings import Finding

finding = Finding(

    host="10.0.9.5",

    port=21,

    service="ftp",

    product="vsFTPd",

    version="2.3.4",

    vendor="vsFTPd Project",

    cpe="cpe:2.3:a:vsftpd:vsftpd:2.3.4:*:*:*:*:*:*:*",

    confidence=100,

    cve="CVE-2011-2523",

    severity="CRITICAL",

    description="Backdoor vulnerability allowing remote shell."

)

print(finding)

print()

print(finding.to_dict())
