from fingerprinting.vendor import VendorDetector

detector = VendorDetector()

products = [

    "vsFTPd",

    "OpenSSH",

    "Apache HTTP Server",

    "PHP",

    "Postfix",

    "Unknown Service"

]

for product in products:

    vendor = detector.detect(product)

    print(f"{product:25} -> {vendor}")
