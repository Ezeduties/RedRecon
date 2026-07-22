"""
======================================================================
EZENOX v1.3.0

Report Builder

Responsibilities
----------------
• Organize findings by service
• Generate executive summary
• Provide structured data for all report formats

Author : Ezeduties
======================================================================
"""


class ReportBuilder:

    def build(self, findings):

        report = {

            "host": "",

            "summary": {

                "services": 0,

                "findings": len(findings),

                "critical": 0,

                "high": 0,

                "medium": 0,

                "low": 0,

                "unknown": 0

            },

            "services": []

        }

        services = {}

        for finding in findings:

            report["host"] = finding.host

            severity = finding.severity.upper()

            if severity == "CRITICAL":

                report["summary"]["critical"] += 1

            elif severity == "HIGH":

                report["summary"]["high"] += 1

            elif severity == "MEDIUM":

                report["summary"]["medium"] += 1

            elif severity == "LOW":

                report["summary"]["low"] += 1

            else:

                report["summary"]["unknown"] += 1

            key = (

                finding.port,

                finding.service

            )

            if key not in services:

                services[key] = {

                    "port": finding.port,

                    "service": finding.service,

                    "vendor": finding.vendor,

                    "product": finding.product,

                    "version": finding.version,

                    "confidence": finding.confidence,

                    "cpe": finding.cpe,

                    "vulnerabilities": []

                }

            services[key]["vulnerabilities"].append({

                "cve": finding.cve,

                "severity": finding.severity,

                "description": finding.description

            })

        report["services"] = list(

            services.values()

        )

        report["summary"]["services"] = len(

            report["services"]

        )

        return report
