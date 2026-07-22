"""
======================================================================
EZENOX v1.3.0

HTTP Evidence Collector

Responsibilities
----------------
• Connect to an HTTP service
• Send an HTTP GET request
• Collect response headers
• Return HTTP evidence

Author : Ezeduties
======================================================================
"""

import socket

from collectors.base import BaseCollector
from evidence.evidence import Evidence


class HTTPCollector(BaseCollector):
    """
    Collect HTTP response headers.
    """

    def collect(self, host, port, service):

        try:

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(self.timeout)

            sock.connect((host, port))

            request = (
                f"GET / HTTP/1.1\r\n"
                f"Host: {host}\r\n"
                f"User-Agent: EZENOX/1.3\r\n"
                f"Connection: close\r\n\r\n"
            )

            sock.send(request.encode())

            response = sock.recv(4096)

            sock.close()

            if not response:

                return None

            response = response.decode(
                errors="ignore"
            )

            return Evidence(

                evidence_type="http",

                host=host,

                port=port,

                protocol="tcp",

                service=service,

                banner=response,

                product="",

                version="",

                confidence=50

            )

        except Exception:

            return None
