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
        Detect loss aversion through recurring high-spend categories.
        """
        if df.empty:
            return DetectionResult(self.BIAS_TYPE, False)

        if "category_rank" not in df.columns or "category_monthly_share" not in df.columns:
            return DetectionResult(self.BIAS_TYPE, False)

        rank = pd.to_numeric(df["category_rank"], errors="coerce").fillna(float("inf"))
        share = pd.to_numeric(df["category_monthly_share"], errors="coerce").fillna(0.0)
        candidate = df.loc[(rank <= 3) & (share >= 0.25)]

        if candidate.empty:
            return DetectionResult(self.BIAS_TYPE, False)

        grouped = candidate.groupby("category").agg(
            recurrence=("category", "size"),
            avg_share=("category_monthly_share", "mean"),
        )
        strong = grouped.loc[grouped["recurrence"] >= 2]

        if strong.empty:
            return DetectionResult(self.BIAS_TYPE, False)

        top_category = str(strong["avg_share"].idxmax())
        top_share = float(strong["avg_share"].max())
        confidence = min(1.0, 0.25 + 0.12 * len(strong))
        severity = "high" if top_share >= 0.5 or len(strong) >= 2 else "medium"
        summary = (
            f"Detected recurring high-spend categories consistent with loss aversion. "
            f"{len(strong)} category(ies) have strong monthly share and top rank."
        )
        if top_category:
            summary = summary + f" Top category: '{top_category}' with average monthly share {top_share:.0%}."

        return DetectionResult(
            self.BIAS_TYPE,
            True,
            confidence=round(confidence, 2),
            severity=severity,
            summary=summary,
            evidence_ids=[],
        )
