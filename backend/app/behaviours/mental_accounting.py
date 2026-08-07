"""
behaviours/mental_accounting.py — Mental Accounting detector.

Mental accounting is the tendency to treat money differently
based on its source or intended use (e.g., spending a bonus
entirely on luxuries while maintaining frugality for salary).

TODO: Implement detection logic.
"""

from __future__ import annotations

import pandas as pd
from app.behaviours.base_detector import BaseBiasDetector, DetectionResult


class MentalAccountingDetector(BaseBiasDetector):
    """Detects mental accounting patterns in spending behaviour."""

    BIAS_TYPE = "mental_accounting"
    DISPLAY_NAME = "Mental Accounting"

    def detect(self, df: pd.DataFrame) -> DetectionResult:
        """
        TODO: Detect spending spikes correlated with large income deposits.
        TODO: Detect disproportionate luxury spend after windfalls.
        TODO: Identify siloed spending patterns by source.
        """
        raise NotImplementedError("MentalAccountingDetector.detect not implemented.")
