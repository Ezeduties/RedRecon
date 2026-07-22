from collectors.ssh import SSHCollector

collector = SSHCollector()

evidence = collector.collect(
    "10.0.9.5",
    22,
    "ssh"
)

if evidence:

    print(evidence)

    print()

    print(evidence.to_dict())

else:

    print("No evidence collected.")
