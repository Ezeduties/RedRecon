
from scanner import Scanner

scanner = Scanner()

result = scanner.scan_host("10.0.9.5")

print("=" * 60)
print("HOST INFORMATION")
print("=" * 60)

print("Host      :", result["host"])
print("Hostname  :", result["hostname"])
print("State     :", result["state"])
print("OS         :", result["os"])

print()

print("=" * 60)
print("OPEN PORTS")
print("=" * 60)

for port in result["ports"]:

    print(
        f'{port["port"]:>5}/'
        f'{port["protocol"]:<3}  '
        f'{port["state"]:<6}  '
        f'{port["service"]:<15}  '
        f'{port["product"]:<20}  '
        f'{port["version"]}'
    )
