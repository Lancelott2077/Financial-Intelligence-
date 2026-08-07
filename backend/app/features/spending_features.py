"""
features/spending_features.py — Amount-based feature extractor.

Computes features related to transaction amounts:
- Z-score within category (outlier detection)
- Rolling 30-day average spend
- Spend velocity (rate of change)
- High-value transaction flag

TODO: Implement all spending feature computations using numpy/pandas.
"""

from __future__ import annotations

import pandas as pd


class SpendingFeatureExtractor:
    """Extracts amount-based spending features from transaction data."""

    def extract(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Add spending feature columns to the transaction DataFrame.

        Args:
            df: Normalised DataFrame with 'amount' and 'category' columns.

        Returns:
            DataFrame with additional spending feature columns.

        TODO: Add amount_zscore_in_category column.
        TODO: Add rolling_30d_avg_spend column.
        TODO: Add spend_velocity column (delta of rolling avg over time).
        TODO: Add is_high_value flag (e.g., > 2 std devs above category mean).
        """
        raise NotImplementedError("SpendingFeatureExtractor.extract not implemented.")
