"""
======================================================================
EZENOX v1.3.0

Dispatcher

Responsibilities
----------------
• Select the correct collector
• Hide collector implementation details
• Provide a single interface to the scanner

Author : Ezeduties
======================================================================
"""

from collectors.ftp import FTPCollector
from collectors.ssh import SSHCollector
from collectors.smtp import SMTPCollector
from collectors.http import HTTPCollector
from collectors.https import HTTPSCollector


class Dispatcher:

    def __init__(self):

        self.collectors = {

            "ftp": FTPCollector(),

            "ssh": SSHCollector(),

            "smtp": SMTPCollector(),

            "http": HTTPCollector(),

            "https": HTTPSCollector()

        }

    def dispatch(self, host, port, service):

        service = service.lower()

        collector = self.collectors.get(service)

        if collector is None:

            return None

        return collector.collect(
            host,
            port,
            service
        )
