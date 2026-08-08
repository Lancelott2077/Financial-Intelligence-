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
        Detect anchoring via low relative amount variance within high-ranked categories.
        """
        if df.empty:
            return DetectionResult(self.BIAS_TYPE, False)

        if "amount_zscore_in_category" not in df.columns or "category_rank" not in df.columns:
            return DetectionResult(self.BIAS_TYPE, False)

        zscore = pd.to_numeric(df["amount_zscore_in_category"], errors="coerce").fillna(0.0)
        rank = pd.to_numeric(df["category_rank"], errors="coerce").fillna(float("inf"))

        candidates = df.loc[(rank <= 3) & (zscore.abs() <= 1.0)]

        if candidates.empty:
            return DetectionResult(self.BIAS_TYPE, False)

        confidence = min(1.0, 0.25 + 0.08 * len(candidates))
        severity = "high" if len(candidates) >= 5 else "medium" if len(candidates) >= 3 else "low"
        summary = (
            f"Detected anchoring-like spending: {len(candidates)} transactions are consistently"
            " clustered near category anchor amounts."
        )

        return DetectionResult(
            self.BIAS_TYPE,
            True,
            confidence=round(confidence, 2),
            severity=severity,
            summary=summary,
            evidence_ids=[],
        )
