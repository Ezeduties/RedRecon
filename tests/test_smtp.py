from collectors.smtp import SMTPCollector

collector = SMTPCollector()

evidence = collector.collect(
    "10.0.9.5",
    25,
    "smtp"
)

if evidence:

    print(evidence)
    print()
    print(evidence.to_dict())

else:

    print("No evidence collected.")
