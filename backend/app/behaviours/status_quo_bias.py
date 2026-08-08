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
        Detect status quo bias through stable high-share categories and low spend velocity.
        """
        if df.empty:
            return DetectionResult(self.BIAS_TYPE, False)

        if "category_monthly_share" not in df.columns or "category_rank" not in df.columns or "spend_velocity" not in df.columns:
            return DetectionResult(self.BIAS_TYPE, False)

        rank = pd.to_numeric(df["category_rank"], errors="coerce").fillna(float("inf"))
        share = pd.to_numeric(df["category_monthly_share"], errors="coerce").fillna(0.0)
        velocity = pd.to_numeric(df["spend_velocity"], errors="coerce").fillna(0.0)

        candidates = df.loc[(rank <= 3) & (share >= 0.2) & (velocity.abs() <= 10.0)]

        if candidates.empty:
            return DetectionResult(self.BIAS_TYPE, False)

        grouped = candidates.groupby("category").agg(
            count=("category", "size"),
            avg_share=("category_monthly_share", "mean"),
        )
        stable = grouped.loc[grouped["count"] >= 2]

        if stable.empty:
            return DetectionResult(self.BIAS_TYPE, False)

        top_category = str(stable["avg_share"].idxmax())
        top_share = float(stable["avg_share"].max())
        confidence = min(1.0, 0.2 + 0.1 * len(stable))
        severity = "high" if top_share >= 0.5 else "medium"
        summary = (
            f"Detected status quo behaviour: {len(stable)} recurring category(ies) with stable spend share."
        )
        if top_category:
            summary += f" Top persistent category: '{top_category}' with average monthly share {top_share:.0%}."

        return DetectionResult(
            self.BIAS_TYPE,
            True,
            confidence=round(confidence, 2),
            severity=severity,
            summary=summary,
            evidence_ids=[],
        )
