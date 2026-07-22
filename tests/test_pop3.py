from collectors.pop3 import POP3Collector

collector = POP3Collector()

evidence = collector.collect(
    "10.0.9.5",
    110,
    "pop3"
)

if evidence:

    print(evidence)
    print()
    print(evidence.to_dict())

else:

    print("No evidence collected.")
