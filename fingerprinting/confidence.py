"""
======================================================================
EZENOX v1.3.0

Confidence Scorer

Responsibilities
----------------
• Score fingerprint confidence
• Rate evidence quality
• Prepare evidence for vulnerability matching

Author : Ezeduties
======================================================================
"""


class ConfidenceScorer:
    """
    Assign confidence scores to detected software.
    """

    def score(
        self,
        product="",
        version="",
        vendor=""
    ):

        score = 0

        if product:
            score += 40

        if version:
            score += 40

        if vendor and vendor != "Unknown":
            score += 20

        if score > 100:
            score = 100

        return score
