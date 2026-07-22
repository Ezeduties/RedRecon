"""
======================================================================
EZENOX v1.3.0

Generic Banner Collector

Responsibilities
----------------
• Open a TCP connection
• Receive a service banner
• Return the decoded banner

Author : Ezeduties
======================================================================
"""

import socket

from collectors.base import BaseCollector


class BannerCollector(BaseCollector):
    """
    Base class for banner-based collectors.
    """

    def collect_banner(self, host, port):

        try:

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(self.timeout)

            sock.connect((host, port))

            banner = sock.recv(1024)

            sock.close()

            if not banner:

                return None

            return banner.decode(
                errors="ignore"
            ).strip()

        except Exception:

            return None
