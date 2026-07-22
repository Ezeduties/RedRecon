from evidence.evidence import Evidence

e = Evidence(
    evidence_type="banner",
    host="10.0.9.5",
    port=21,
    protocol="tcp",
    service="ftp",
    banner="220 (vsFTPd 2.3.4)",
    product="vsFTPd",
    version="2.3.4",
    confidence=100,
)

print(e)
print(e.to_dict())
