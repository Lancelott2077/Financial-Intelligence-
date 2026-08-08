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
        Detect mental accounting patterns through category concentration.
        """
        if df.empty:
            return DetectionResult(self.BIAS_TYPE, False)

        if "category_monthly_share" not in df.columns:
            return DetectionResult(self.BIAS_TYPE, False)

        share = pd.to_numeric(df["category_monthly_share"], errors="coerce").fillna(0.0)
        max_share = float(share.max())

        if max_share < 0.3:
            return DetectionResult(self.BIAS_TYPE, False)

        top_idx = share.idxmax()
        top_category = None
        if "category" in df.columns and top_idx in df.index:
            top_category = str(df.loc[top_idx, "category"])

        confidence = min(1.0, 0.2 + max_share)
        severity = "high" if max_share >= 0.5 else "medium"
        summary = (
            f"Detected mental accounting patterns with a single category"
            f" accounting for {max_share:.0%} of monthly spend."
        )
        if top_category:
            summary = summary.replace(
                "a single category",
                f"'{top_category}'"
            )

        return DetectionResult(
            self.BIAS_TYPE,
            True,
            confidence=round(confidence, 2),
            severity=severity,
            summary=summary,
            evidence_ids=[],
        )
