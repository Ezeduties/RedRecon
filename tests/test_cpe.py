from fingerprinting.cpe_generator import CPEGenerator

generator = CPEGenerator()

samples = [

    (
        "Apache Software Foundation",
        "Apache HTTP Server",
        "2.2.8"
    ),

    (
        "OpenBSD Project",
        "OpenSSH",
        "4.7p1"
    ),

    (
        "PHP Group",
        "PHP",
        "5.2.4"
    ),

    (
        "vsFTPd Project",
        "vsFTPd",
        "2.3.4"
    ),

    (
        "Postfix Project",
        "Postfix",
        ""
    )

]

for vendor, product, version in samples:

    cpe = generator.generate(
        vendor,
        product,
        version
    )

    print(cpe)
