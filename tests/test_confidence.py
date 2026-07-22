from fingerprinting.confidence import ConfidenceScorer

scorer = ConfidenceScorer()

samples = [

    ("vsFTPd", "2.3.4", "vsFTPd Project"),

    ("Apache HTTP Server", "", "Apache Software Foundation"),

    ("OpenSSH", "4.7p1", "Unknown"),

    ("", "", "")

]

for product, version, vendor in samples:

    score = scorer.score(
        product,
        version,
        vendor
    )

    print("=" * 60)

    print(product)

    print(version)

    print(vendor)

    print(f"Confidence: {score}%")
