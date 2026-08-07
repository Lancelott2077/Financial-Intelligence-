"""
features/merchant_features.py — Merchant recurrence and loyalty feature extractor.

Computes features related to merchant-level behaviour:
- Visit frequency per merchant
- Average spend per merchant visit
- Merchant loyalty score (% of category spend at single merchant)
"""

from __future__ import annotations

import pandas as pd
import numpy as np


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
        # Ensure required columns exist
        if df.empty or not {"merchant", "amount", "date", "category"}.issubset(df.columns):
            return df

        df_feat = df.copy()
        
        # Initialize output columns safely
        df_feat["merchant_visit_frequency"] = np.nan
        df_feat["merchant_avg_spend"] = np.nan
        df_feat["merchant_loyalty_score"] = 0.0

        # Create mask for valid merchants
        # Handle actual nulls and empty strings
        valid_merchant = df_feat["merchant"].notna() & (df_feat["merchant"].astype(str).str.strip() != "")
        
        if not valid_merchant.any():
            return df_feat

        # Extract only the valid rows for grouped calculations
        df_valid = df_feat[valid_merchant].copy()
        
        # Use absolute amount to standardize magnitude aggregations
        df_valid["abs_amount"] = df_valid["amount"].abs()

        # 1. Merchant Visit Frequency (visits per month)
        days_active = (df_feat["date"].max() - df_feat["date"].min()).days
        months_active = max(1.0, days_active / 30.44)
        
        merchant_counts = df_valid.groupby("merchant")["merchant"].transform("count")
        df_feat.loc[valid_merchant, "merchant_visit_frequency"] = merchant_counts / months_active

        # 2. Merchant Average Spend
        merchant_avg = df_valid.groupby("merchant")["abs_amount"].transform("mean")
        df_feat.loc[valid_merchant, "merchant_avg_spend"] = merchant_avg

        # 3. Merchant Loyalty Score (% of category spend)
        # Total absolute spend for the specific merchant within the specific category
        merchant_cat_spend = df_valid.groupby(["category", "merchant"])["abs_amount"].transform("sum")
        
        # Total absolute spend for the entire category across all rows (including null merchants)
        cat_spend = df_feat.groupby("category")["amount"].transform(lambda x: x.abs().sum())
        
        # Map category spend strictly to the valid merchant rows using index alignment
        cat_spend_valid = cat_spend[valid_merchant]
        
        # Compute ratio (0.0 to 1.0) and handle division by zero
        loyalty_score = (merchant_cat_spend / cat_spend_valid).fillna(0.0)
        df_feat.loc[valid_merchant, "merchant_loyalty_score"] = loyalty_score
            
        return df_feat
