"""
behaviours/anchoring.py — Anchoring bias detector.

Anchoring is the tendency to rely heavily on the first piece of
information (the "anchor") when making decisions, e.g., always
spending approximately the same amount at a merchant regardless
of current needs.

TODO: Implement detection logic.
"""

from __future__ import annotations

import pandas as pd
from app.behaviours.base_detector import BaseBiasDetector, DetectionResult


class AnchoringDetector(BaseBiasDetector):
    """Detects anchoring bias in spending amounts."""

    BIAS_TYPE = "anchoring"
    DISPLAY_NAME = "Anchoring Bias"

    def detect(self, df: pd.DataFrame) -> DetectionResult:
        """
        TODO: Detect low variance in spend amounts per merchant.
        TODO: Detect habitual round-number spending.
        TODO: Compare anchor amounts to market alternatives.
        """
        raise NotImplementedError("AnchoringDetector.detect not implemented.")
