"""
======================================================================
EZENOX v1.3.0

Banner Parser

Responsibilities
----------------
• Parse common service banners
• Extract product names
• Extract version numbers

Author : Ezeduties
======================================================================
"""

import re


class BannerParser:
    """
    Parse banners collected from services.
    """

    PATTERNS = [

        (
            re.compile(
                r"vsFTPd\s+([0-9.]+)",
                re.IGNORECASE
            ),
            "vsFTPd"
        ),

        (
            re.compile(
                r"OpenSSH[_ ]([0-9.p]+)",
                re.IGNORECASE
            ),
            "OpenSSH"
        ),

        (
            re.compile(
                r"Postfix",
                re.IGNORECASE
            ),
            "Postfix"
        ),

        (
            re.compile(
                r"Apache/?([0-9.]+)",
                re.IGNORECASE
            ),
            "Apache HTTP Server"
        ),

        (
            re.compile(
                r"PHP/?([0-9.\-a-z]+)",
                re.IGNORECASE
            ),
            "PHP"
        )

    ]

    def parse(self, banner):

        result = {

            "product": "",
            "version": ""

        }

        if not banner:

            return result

        for pattern, product in self.PATTERNS:

            match = pattern.search(banner)

            if match:

                result["product"] = product

                if match.lastindex:

                    result["version"] = match.group(1)

                return result

        return result
