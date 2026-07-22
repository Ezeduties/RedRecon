from collectors.imap import IMAPCollector

collector = IMAPCollector()

evidence = collector.collect(
    "10.0.9.5",
    143,
    "imap"
)

if evidence:

    print(evidence)
    print()
    print(evidence.to_dict())

else:

    print("No evidence collected.")
