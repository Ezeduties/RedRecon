from collectors.ftp import FTPCollector

collector = FTPCollector()

evidence = collector.collect(
    "10.0.9.5",
    21,
    "ftp"
)

if evidence:

    print(evidence)

    print()

    print(evidence.to_dict())

else:

    print("No evidence collected.")
