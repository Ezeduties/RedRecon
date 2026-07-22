"""
=========================================================
EZENOX Evidence Model

Author : Ezeduties
Version: 1.3.0

Description
-----------
Represents a single piece of evidence collected during
reconnaissance or vulnerability assessment.

All future evidence modules (Banner, HTTP, TLS, SMB,
SNMP, SSH, etc.) will use this model.
=========================================================
"""

from dataclasses import dataclass, asdict


@dataclass
class Evidence:
    """
    Represents one piece of collected evidence.
    """

    evidence_type: str
    host: str
    port: int
    protocol: str
    service: str

    banner: str = ""

    product: str = ""

    version: str = ""

    confidence: int = 0

    def to_dict(self):
        """
        Convert the object into a dictionary.
        """

        return asdict(self)
