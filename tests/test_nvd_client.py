from vulnerability.nvd_client import NVDClient

client = NVDClient()

results = client.search(

    cpe="cpe:2.3:a:vsftpd:vsftpd:2.3.4:*:*:*:*:*:*:*",

    product="vsFTPd",

    version="2.3.4"

)

print()

print(f"Found {len(results)} vulnerabilities.\n")

for item in results[:5]:

    print("=" * 60)

    print(item["cve"])

    print(item["severity"])

    print(item["description"])
