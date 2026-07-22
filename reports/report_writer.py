"""
=========================================================
EZENOX Report Module

Generates professional reports from scan results.

Supported Formats
    • CSV
    • JSON
    • TXT

Author : Ezeduties
Version: 1.1.0
=========================================================
"""

# --------------------------------------------------------
# Standard Library Imports
# --------------------------------------------------------

import csv
import json

# --------------------------------------------------------
# Local Imports
# --------------------------------------------------------

from utils.helpers import (
    create_reports_directory,
    get_timestamp,
    save_text_file,
    print_line,
)

# --------------------------------------------------------
# Report Generator
# --------------------------------------------------------

class ReportGenerator:
    """
    Generates reports from EZENOX scan results.

    Supports:

        • Single Host Scan

        • Multiple Host Scan
    """

    # ----------------------------------------------------
    # Constructor
    # ----------------------------------------------------

    def __init__(self, scan_results):

        # Always store results as a list

        if isinstance(scan_results, dict):

            self.scan_results = [scan_results]

        else:

            self.scan_results = scan_results

        self.reports_directory = create_reports_directory()

        self.timestamp = get_timestamp()

    # ----------------------------------------------------
    # CSV REPORT
    # ----------------------------------------------------

    def save_csv(self):

        filename = (
            self.reports_directory /
            f"scan_{self.timestamp}.csv"
        )

        with open(
            filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow([
                "IP Address",
                "Hostname",
                "State",
                "Operating System",
                "Port",
                "Protocol",
                "Port State",
                "Service",
                "Product",
                "Version"
            ])

            # -----------------------------------------
            # Every scanned host
            # -----------------------------------------

            for host in self.scan_results:

                ip = host.get("host", "")

                hostname = host.get("hostname", "")

                state = host.get("state", "")

                os_name = host.get("os", "")

                ports = host.get("ports", [])

                # -------------------------------------
                # Host with no open ports
                # -------------------------------------

                if not ports:

                    writer.writerow([
                        ip,
                        hostname,
                        state,
                        os_name,
                        "",
                        "",
                        "",
                        "",
                        "",
                        ""
                    ])

                    continue

                # -------------------------------------
                # Host with open ports
                # -------------------------------------

                for port in ports:

                    writer.writerow([

                        ip,

                        hostname,

                        state,

                        os_name,

                        port.get("port", ""),

                        port.get("protocol", ""),

                        port.get("state", ""),

                        port.get("service", ""),

                        port.get("product", ""),

                        port.get("version", "")

                    ])

        return filename

    # ----------------------------------------------------
    # JSON REPORT
    # ----------------------------------------------------

    def save_json(self):
        """
        Save scan results as JSON.
        """

        filename = (
            self.reports_directory /
            f"scan_{self.timestamp}.json"
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as jsonfile:

            json.dump(
                self.scan_results,
                jsonfile,
                indent=4
            )

        return filename


    # ----------------------------------------------------
    # TEXT REPORT
    # ----------------------------------------------------

    def save_text(self):
        """
        Save a human-readable text report.
        """

        report = []

        report.append("=" * 60)
        report.append("EZENOX SCAN REPORT")
        report.append("=" * 60)
        report.append("")

        for host in self.scan_results:

            report.append(f"IP Address : {host.get('host', '')}")
            report.append(f"Hostname   : {host.get('hostname', '')}")
            report.append(f"State      : {host.get('state', '')}")
            report.append(f"OS         : {host.get('os', '')}")

            report.append("")
            report.append("-" * 60)
            report.append("OPEN PORTS")
            report.append("-" * 60)

            ports = host.get("ports", [])

            if not ports:

                report.append("No open ports discovered.")

            else:

                for port in ports:

                    line = (
                        f"{port.get('port',''):>5}/"
                        f"{port.get('protocol','')}  "
                        f"{port.get('state',''):8} "
                        f"{port.get('service',''):15} "
                        f"{port.get('product',''):20} "
                        f"{port.get('version','')}"
                    )

                    report.append(line)

            report.append("")
            report.append("=" * 60)
            report.append("")

        report_text = "\n".join(report)

        filename = f"scan_{self.timestamp}.txt"

        return save_text_file(filename, report_text)

    # ----------------------------------------------------
    # EXPORT ALL REPORTS
    # ----------------------------------------------------

    def export_all(self):
        """
        Export all report formats.

        Returns
        -------
        dict
            Dictionary containing generated report paths.
        """

        return {

            "csv": self.save_csv(),

            "json": self.save_json(),

            "txt": self.save_text()

        }


# --------------------------------------------------------
# Standalone Test
# --------------------------------------------------------

if __name__ == "__main__":

    sample_scan = [

        {

            "ip": "10.0.9.5",

            "hostname": "Metasploitable2",

            "state": "up",

            "os": "Linux 2.6.9",

            "ports": [

                {

                    "port": 21,

                    "protocol": "tcp",

                    "state": "open",

                    "service": "ftp",

                    "product": "vsftpd",

                    "version": "2.3.4"

                },

                {

                    "port": 22,

                    "protocol": "tcp",

                    "state": "open",

                    "service": "ssh",

                    "product": "OpenSSH",

                    "version": "4.7p1"

                }

            ]

        },

        {

            "ip": "10.0.9.6",

            "hostname": "",

            "state": "down",

            "os": "Unknown",

            "ports": []

        }

    ]

    report = ReportGenerator(sample_scan)

    reports = report.export_all()

    print_line()

    print("Reports Generated Successfully\n")

    for report_type, path in reports.items():

        print(f"{report_type.upper():5} -> {path}")

    print_line()
