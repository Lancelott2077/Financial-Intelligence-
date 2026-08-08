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
        - Impulse purchases (high-value, non-essential, weekend transactions).
        """
        if df.empty:
            return DetectionResult(self.BIAS_TYPE, False)

        if "days_from_payday" not in df.columns or "is_high_value" not in df.columns:
            return DetectionResult(self.BIAS_TYPE, False)

        days = pd.to_numeric(df["days_from_payday"], errors="coerce").abs().fillna(float("inf"))
        high_value = df["is_high_value"].astype(bool)
        near_payday = days <= 3
        candidates = df.loc[high_value & near_payday]

        if candidates.empty:
            return DetectionResult(self.BIAS_TYPE, False)

        confidence = min(1.0, 0.35 + 0.08 * len(candidates))
        if "is_weekend" in candidates.columns and candidates["is_weekend"].astype(bool).any():
            confidence = min(1.0, confidence + 0.1)

        severity = "high" if confidence >= 0.75 else "medium" if confidence >= 0.5 else "low"
        summary = (
            f"Detected high-value spending near payday. "
            f"{len(candidates)} recent transaction(s) match impulsive spending patterns."
        )

        return DetectionResult(
            self.BIAS_TYPE,
            True,
            confidence=round(confidence, 2),
            severity=severity,
            summary=summary,
            evidence_ids=[],
        )
