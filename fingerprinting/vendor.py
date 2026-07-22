"""
======================================================================
EZENOX v1.3.0

Vendor Detector

Responsibilities
----------------
• Map products to vendors
• Normalize product names
• Prepare data for CPE generation

Author : Ezeduties
======================================================================
"""


class VendorDetector:
    """
    Detect vendor names from identified products.
    """

    VENDORS = {

        "vsFTPd": "vsFTPd Project",

        "OpenSSH": "OpenBSD Project",

        "Apache HTTP Server": "Apache Software Foundation",

        "PHP": "PHP Group",

        "Postfix": "Postfix Project",

        "Microsoft IIS": "Microsoft",

        "nginx": "NGINX, Inc.",

        "Samba": "Samba Team"

    }

    def detect(self, product):

        return self.VENDORS.get(
            product,
            "Unknown"
        )
