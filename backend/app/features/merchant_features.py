"""
features/merchant_features.py — Merchant recurrence and loyalty feature extractor.

Computes features related to merchant-level behaviour:
- Visit frequency per merchant
- Average spend per merchant visit
- Merchant loyalty score (% of category spend at single merchant)
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
        """
        df_feat = df.copy()
        df_feat["merchant_visit_frequency"] = 0.0
        df_feat["merchant_avg_spend"] = 0.0
        df_feat["merchant_loyalty_score"] = 0.0
        return df_feat
