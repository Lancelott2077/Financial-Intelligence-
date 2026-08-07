"""
behaviours/loss_aversion.py — Loss Aversion detector.

Loss aversion is the tendency to prefer avoiding losses over acquiring
equivalent gains, often manifesting as over-spending on insurance,
hedging, or holding onto subscriptions out of fear of losing access.

TODO: Implement detection logic.
"""

from __future__ import annotations

import pandas as pd
from app.behaviours.base_detector import BaseBiasDetector, DetectionResult


class LossAversionDetector(BaseBiasDetector):
    """Detects loss aversion patterns in spending behaviour."""

    BIAS_TYPE = "loss_aversion"
    DISPLAY_NAME = "Loss Aversion"

    def detect(self, df: pd.DataFrame) -> DetectionResult:
        """
        TODO: Detect over-spending on subscriptions and insurance.
        TODO: Detect continued payments after trial period ends.
        TODO: Detect avoidance of switching to cheaper alternatives.
        """
        raise NotImplementedError("LossAversionDetector.detect not implemented.")
