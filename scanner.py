"""
======================================================================
RedRecon v1.0.0
Professional Network Reconnaissance Framework

Author      : Ezeduties
Version     : 1.0.0
Python      : 3.x

Description
-----------
This module is responsible for interacting with the Nmap engine.
It performs host scanning and returns structured scan results
to the rest of the RedRecon framework.

======================================================================
"""

# ==========================================================
# Imports
# ==========================================================

from nmap import PortScanner


# ==========================================================
# Scanner Class
# ==========================================================

class Scanner:
    """
    Handles all Nmap scanning operations.
    """

    def __init__(self):
        """
        Create a PortScanner object once.

        Every scan performed by this class will reuse
        the same scanner instance.
        """

        self.nm = PortScanner()


# ======================================================
# Scan One Host
# ======================================================

    def scan_host(self, target):
        """
        Scan a single host using Nmap.

        Parameters
        ----------
        target : str
            IPv4 Address

        Returns
        -------
        dict
            Structured scan results.
        """

        scan_arguments = "-Pn -sV -O"

        self.nm.scan(hosts=target, arguments=scan_arguments)

        result = {
            "host": target,
            "hostname": "",
            "state": "",
            "os": "Unknown",
            "ports": []
        }

        # ---------------------------------------------
        # Host Information
        # ---------------------------------------------

        result["hostname"] = self.nm[target].hostname()
        result["state"] = self.nm[target].state()

        # ---------------------------------------------
        # Operating System Detection
        # ---------------------------------------------

        if "osmatch" in self.nm[target]:

            os_matches = self.nm[target]["osmatch"]

            if os_matches:

                result["os"] = os_matches[0]["name"]

        # ---------------------------------------------
        # Parse Protocols and Ports
        # ---------------------------------------------

        for protocol in self.nm[target].all_protocols():

            ports = sorted(self.nm[target][protocol].keys())

            for port in ports:

                service = self.nm[target][protocol][port]

                port_info = {

                    "port": port,

                    "protocol": protocol,

                    "state": service.get("state", ""),

                    "service": service.get("name", ""),

                    "product": service.get("product", ""),

                    "version": service.get("version", "")

                }

                result["ports"].append(port_info)

        return result
