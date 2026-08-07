"""
features/category_features.py — Category share and drift feature extractor.

Computes features at the spending category level:
- Category share of total monthly spend
- Month-over-month category spend drift
- Budget adherence ratio (if budget data available)

TODO: Implement all category-level feature computations.
"""

from __future__ import annotations

import pandas as pd


class CategoryFeatureExtractor:
    """Extracts category-level share and drift features."""

    def extract(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Add category-level feature columns to the transaction DataFrame.

        Args:
            df: Normalised DataFrame with 'category', 'amount', 'date' columns.

        Returns:
            DataFrame with additional category feature columns.

        TODO: Add category_monthly_share (% of total monthly spend).
        TODO: Add category_mom_drift (month-over-month % change in category spend).
        TODO: Add category_rank (rank of category by spend per month).
        """
        raise NotImplementedError("CategoryFeatureExtractor.extract not implemented.")
