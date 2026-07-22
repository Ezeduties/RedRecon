"""
======================================================================
EZENOX v1.3.0

HTTP Response Parser

Responsibilities
----------------
• Parse HTTP status line
• Parse HTTP headers
• Return structured information

Author : Ezeduties
======================================================================
"""


class HTTPParser:
    """
    Parse raw HTTP responses.
    """

    def parse(self, response):

        result = {

            "status_code": None,
            "reason": "",
            "server": "",
            "powered_by": "",
            "content_type": "",
            "content_length": "",
            "headers": {}

        }

        if not response:

            return result

        lines = response.split("\r\n")

        # -----------------------------
        # Parse Status Line
        # -----------------------------

        if lines:

            status = lines[0].split()

            if len(status) >= 3:

                result["status_code"] = int(status[1])

                result["reason"] = " ".join(status[2:])

        # -----------------------------
        # Parse Headers
        # -----------------------------

        for line in lines[1:]:

            if not line:

                break

            if ":" not in line:

                continue

            key, value = line.split(":", 1)

            key = key.strip()

            value = value.strip()

            result["headers"][key] = value

        result["server"] = result["headers"].get("Server", "")

        result["powered_by"] = result["headers"].get(
            "X-Powered-By", ""
        )

        result["content_type"] = result["headers"].get(
            "Content-Type", ""
        )

        result["content_length"] = result["headers"].get(
            "Content-Length", ""
        )

        return result
