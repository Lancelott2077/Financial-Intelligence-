"""
features/merchant_features.py — Merchant recurrence and loyalty feature extractor.

Computes features related to merchant-level behaviour:
- Visit frequency per merchant
- Average spend per merchant visit
- Merchant loyalty score (% of category spend at single merchant)

TODO: Implement all merchant feature computations.
"""

from __future__ import annotations

import pandas as pd


class MerchantFeatureExtractor:
    """Extracts merchant-level recurrence and loyalty features."""

    def extract(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Add merchant feature columns to the transaction DataFrame.

        Args:
            df: Normalised DataFrame with 'merchant' and 'category' columns.

        Returns:
            DataFrame with additional merchant feature columns.

        TODO: Add merchant_visit_frequency (visits per month).
        TODO: Add merchant_avg_spend.
        TODO: Add merchant_loyalty_score (% of category spend).
        TODO: Handle null merchant values gracefully.
        """
        raise NotImplementedError("MerchantFeatureExtractor.extract not implemented.")
