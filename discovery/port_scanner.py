"""
======================================================================
EZENOX v1.3.0

Professional Network Reconnaissance Framework

Scanner Engine

Responsibilities
----------------
• Execute Nmap scans
• Parse host information
• Parse services
• Dispatch protocol collectors
• Attach evidence to services

Author : Ezeduties
======================================================================
"""

from nmap import PortScanner

from core.dispatcher import Dispatcher


class Scanner:

    def __init__(self):

        self.nm = PortScanner()

        self.dispatcher = Dispatcher()

    def scan_host(self, target):

        scan_arguments = "-Pn -sV -O"

        self.nm.scan(
            hosts=target,
            arguments=scan_arguments
        )

        result = {

            "host": target,

            "hostname": "",

            "state": "down",

            "reason": "Host unreachable",

            "os": "Unknown",

            "ports": []

        }

        if target not in self.nm.all_hosts():

            return result

        host = self.nm[target]

        result["hostname"] = host.hostname()

        result["state"] = host.state()

        # ----------------------------
        # Operating System Detection
        # ----------------------------

        if "osmatch" in host:

            osmatch = host["osmatch"]

            if osmatch:

                result["os"] = osmatch[0]["name"]

        # ----------------------------
        # Parse Protocols
        # ----------------------------

        for protocol in host.all_protocols():

            for port in sorted(host[protocol].keys()):

                service = host[protocol][port]

                service_name = service.get(
                    "name",
                    ""
                ).lower()

                port_info = {

                    "port": port,

                    "protocol": protocol,

                    "state": service.get(
                        "state",
                        ""
                    ),

                    "service": service_name,

                    "product": service.get(
                        "product",
                        ""
                    ),

                    "version": service.get(
                        "version",
                        ""
                    ),

                    "evidence": []

                }

                # ------------------------
                # Evidence Collection
                # ------------------------

                if port_info["state"] == "open":

                    evidence = self.dispatcher.dispatch(

                        target,

                        port,

                        service_name

                    )

                    if evidence:

                        port_info["evidence"].append(

                            evidence.to_dict()

                        )

                result["ports"].append(

                    port_info

                )

        return result
