"""
=========================================================
RedRecon Report Module

Generates professional reports from scan results.

Supported Formats:
    - CSV
    - JSON
    - TXT

Author : Ezeduties
Version: 1.0
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

from utils import (
    create_reports_directory,
    get_timestamp,
    save_text_file,
    print_line
)


# --------------------------------------------------------
# Report Generator Class
# --------------------------------------------------------

class ReportGenerator:
    """
    Generates professional reports from
    RedRecon scan results.
    """

    # ----------------------------------------------------
    # Constructor
    # ----------------------------------------------------

    def __init__(self, scan_results):
        """
        Initialize the Report Generator.

        Parameters
        ----------
        scan_results : dict
            Dictionary returned by Scanner.
        """

        self.scan_results = scan_results
        self.reports_directory = create_reports_directory()
        self.timestamp = get_timestamp()

    # ----------------------------------------------------
    # Save CSV Report
    # ----------------------------------------------------

    def save_csv(self):
        """
        Save scan results to CSV format.

        Returns
        -------
        Path
            CSV report path.
        """

        filename = self.reports_directory / f"scan_{self.timestamp}.csv"

        with open(filename, "w", newline="", encoding="utf-8") as csvfile:

            writer = csv.writer(csvfile)

            # CSV Header
            writer.writerow([
                "IP Address",
                "Hostname",
                "Host State",
                "Operating System",
                "Port",
                "Protocol",
                "Port State",
                "Service",
                "Product",
                "Version"
            ])

            ip = self.scan_results.get("ip", "")
            hostname = self.scan_results.get("hostname", "")
            state = self.scan_results.get("state", "")
            os_name = self.scan_results.get("os", "")

            ports = self.scan_results.get("ports", [])

            # If no ports were found
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

            else:

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
    # Save JSON Report
    # ----------------------------------------------------

    def save_json(self):
        """
        Save scan results as JSON.

        Returns
        -------
        Path
            JSON report path.
        """

        filename = self.reports_directory / f"scan_{self.timestamp}.json"

        with open(filename, "w", encoding="utf-8") as jsonfile:

            json.dump(
                self.scan_results,
                jsonfile,
                indent=4
            )

        return filename
    # ----------------------------------------------------
    # Save Text Report
    # ----------------------------------------------------

    def save_text(self):
        """
        Save scan results as a human-readable text report.

        Returns
        -------
        Path
            Text report path.
        """

        report = []

        report.append("=" * 60)
        report.append("REDRECON SCAN REPORT")
        report.append("=" * 60)

        report.append(f"IP Address : {self.scan_results.get('ip','')}")
        report.append(f"Hostname   : {self.scan_results.get('hostname','')}")
        report.append(f"State      : {self.scan_results.get('state','')}")
        report.append(f"OS         : {self.scan_results.get('os','')}")
        report.append("")

        report.append("=" * 60)
        report.append("OPEN PORTS")
        report.append("=" * 60)

        ports = self.scan_results.get("ports", [])

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

        report_text = "\n".join(report)

        filename = f"scan_{self.timestamp}.txt"

        return save_text_file(filename, report_text)

    # ----------------------------------------------------
    # Export Everything
    # ----------------------------------------------------

    def export_all(self):
        """
        Export all report formats.

        Returns
        -------
        dict
            Dictionary containing all report paths.
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

    sample_scan = {

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
    }

    report = ReportGenerator(sample_scan)

    files = report.export_all()

    print_line()

    print("Reports Generated Successfully\n")

    for report_type, path in files.items():
        print(f"{report_type.upper():5} -> {path}")

    print_line()
