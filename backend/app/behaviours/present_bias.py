"""
behaviours/present_bias.py — Present Bias detector.

Present bias is the tendency to prefer smaller immediate rewards
over larger future rewards, manifesting as impulsive spending
near payday and low savings rates.

TODO: Implement detection logic using temporal and spending features.
"""

from __future__ import annotations

import pandas as pd

from app.behaviours.base_detector import BaseBiasDetector, DetectionResult


class PresentBiasDetector(BaseBiasDetector):
    """Detects present bias (short-term preference over long-term saving)."""

    BIAS_TYPE = "present_bias"
    DISPLAY_NAME = "Present Bias"

    def detect(self, df: pd.DataFrame) -> DetectionResult:
        """
        Detect present bias signals in the transaction data.

        Signals to look for:
        - High spend in entertainment/dining categories near payday.
        - Low or zero savings rate.
        - Impulse purchases (high-value, non-essential, weekend transactions).

        TODO: Implement signal computation using feature columns.
        TODO: Aggregate signals into a confidence score.
        TODO: Identify top evidence transactions.
        """
        raise NotImplementedError("PresentBiasDetector.detect not implemented.")
