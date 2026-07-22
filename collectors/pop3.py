"""
======================================================================
EZENOX v1.3.0

POP3 Evidence Collector
======================================================================
"""

from collectors.banner import BannerCollector
from evidence.evidence import Evidence


class POP3Collector(BannerCollector):
    """
    Collect POP3 banner evidence.
    """

    def collect(self, host, port, service):

        banner = self.collect_banner(host, port)

        if not banner:
            return None

        return Evidence(

            evidence_type="banner",

            host=host,

            port=port,

            protocol="tcp",

            service=service,

            banner=banner,

            product="",

            version="",

            confidence=50

        )
