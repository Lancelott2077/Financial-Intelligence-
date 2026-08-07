"""
behaviours/status_quo_bias.py — Status Quo Bias detector.

Status quo bias is the preference for the current state of affairs,
manifesting as continued subscription payments, habitual purchases
at the same stores even when cheaper alternatives exist.

TODO: Implement detection logic.
"""

from __future__ import annotations

import pandas as pd
from app.behaviours.base_detector import BaseBiasDetector, DetectionResult


class StatusQuoBiasDetector(BaseBiasDetector):
    """Detects status quo / inertia patterns."""

    BIAS_TYPE = "status_quo_bias"
    DISPLAY_NAME = "Status Quo Bias"

    def detect(self, df: pd.DataFrame) -> DetectionResult:
        """
        TODO: Detect recurring fixed-amount transactions (subscriptions).
        TODO: Detect habitual merchant loyalty without alternatives explored.
        TODO: Detect high merchant_loyalty_score in low-necessity categories.
        """
        raise NotImplementedError("StatusQuoBiasDetector.detect not implemented.")
