from collectors.http import HTTPCollector

collector = HTTPCollector()

evidence = collector.collect(
    "10.0.9.5",
    80,
    "http"
)

if evidence:

    print(evidence)
    print()
    print(evidence.to_dict())

else:

    print("No evidence collected.")
