from validator import validate_targets

target = input("Enter Target: ")

valid, invalid = validate_targets(target)

print("\nVALID TARGETS")

for host in valid:

    print(host)

print("\nINVALID TARGETS")

for host in invalid:

    print(host)
