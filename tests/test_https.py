from collectors.https import HTTPSCollector

collector = HTTPSCollector()

evidence = collector.collect(
    "10.0.9.5",
    443,
    "https"
)

if evidence:

    print(evidence)
    print()
    print(evidence.to_dict())

else:

    print("No evidence collected.")
