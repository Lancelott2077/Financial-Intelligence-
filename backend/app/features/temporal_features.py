"""
features/temporal_features.py — Time-based feature extractor.

Computes features related to when transactions occur:
- Day of week (0=Monday, 6=Sunday)
- Is weekend flag
- Is payday proximity flag
- Time since last transaction in same category

TODO: Implement all temporal feature computations.
"""

from __future__ import annotations

import pandas as pd


class TemporalFeatureExtractor:
    """Extracts time-based features from transaction data."""

    def extract(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Add temporal feature columns to the transaction DataFrame.

        Args:
            df: Normalised DataFrame with a 'date' column.

        Returns:
            DataFrame with additional temporal feature columns.

        TODO: Add day_of_week column (0–6).
        TODO: Add is_weekend boolean column.
        TODO: Add days_from_payday column (detect payday from income transactions).
        TODO: Add days_since_last_purchase_in_category column.
        """
        raise NotImplementedError("TemporalFeatureExtractor.extract not implemented.")
