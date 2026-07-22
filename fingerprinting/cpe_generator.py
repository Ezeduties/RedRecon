"""
======================================================================
EZENOX v1.3.0

CPE Generator

Responsibilities
----------------
• Generate CPE 2.3 identifiers
• Normalize vendor and product names
• Prepare identifiers for vulnerability matching

Author : Ezeduties
======================================================================
"""


class CPEGenerator:
    """
    Generate CPE 2.3 strings.
    """

    VENDOR_MAP = {

        "Apache Software Foundation": "apache",

        "OpenBSD Project": "openbsd",

        "PHP Group": "php",

        "Postfix Project": "postfix",

        "vsFTPd Project": "vsftpd",

        "Microsoft": "microsoft",

        "NGINX, Inc.": "nginx",

        "Samba Team": "samba"

    }

    PRODUCT_MAP = {

        "Apache HTTP Server": "http_server",

        "OpenSSH": "openssh",

        "PHP": "php",

        "Postfix": "postfix",

        "vsFTPd": "vsftpd",

        "Microsoft IIS": "internet_information_server",

        "nginx": "nginx",

        "Samba": "samba"

    }

    def generate(self, vendor, product, version):

        vendor_id = self.VENDOR_MAP.get(
            vendor,
            vendor.lower().replace(" ", "_")
        )

        product_id = self.PRODUCT_MAP.get(
            product,
            product.lower().replace(" ", "_")
        )

        version = version or "*"

        return (
            f"cpe:2.3:a:"
            f"{vendor_id}:"
            f"{product_id}:"
            f"{version}:"
            "*:*:*:*:*:*:*"
        )
