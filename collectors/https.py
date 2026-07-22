"""
======================================================================
EZENOX v1.3.0

HTTPS Evidence Collector

Responsibilities
----------------
• Connect to an HTTPS service
• Perform a TLS handshake
• Send an HTTP GET request
• Collect response headers

Author : Ezeduties
======================================================================
"""

import socket
import ssl

from collectors.base import BaseCollector
from evidence.evidence import Evidence


class HTTPSCollector(BaseCollector):
    """
    Collect HTTPS response headers.
    """

    def collect(self, host, port, service):

        try:

            context = ssl.create_default_context()

            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE

            sock = socket.create_connection(
                (host, port),
                timeout=self.timeout
            )

            tls = context.wrap_socket(
                sock,
                server_hostname=host
            )

            request = (
                f"GET / HTTP/1.1\r\n"
                f"Host: {host}\r\n"
                f"User-Agent: EZENOX/1.3\r\n"
                f"Connection: close\r\n\r\n"
            )

            tls.send(request.encode())

            response = tls.recv(4096)

            tls.close()

            if not response:

                return None

            response = response.decode(
                errors="ignore"
            )

            return Evidence(

                evidence_type="https",

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
