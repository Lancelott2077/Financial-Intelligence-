"""
features/spending_features.py — Amount-based feature extractor.

Computes features related to transaction amounts:
- Z-score within category (outlier detection)
- Rolling 30-day average spend
- Spend velocity (rate of change)
- High-value transaction flag
"""

from __future__ import annotations

import pandas as pd
import numpy as np


class SpendingFeatureExtractor:
    """Extracts amount-based spending features from transaction data."""

    def extract(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Add spending feature columns to the transaction DataFrame.

        Args:
            df: Normalised DataFrame with 'amount' and 'category' columns.

        Returns:
            DataFrame with additional spending feature columns.
        """
        if df.empty or "amount" not in df.columns:
            return df
            
        df_feat = df.copy()
        
        # We work with absolute amounts to uniformly treat both large expenses and large incomes 
        # as "high value" outliers, conforming to the "> 2 std devs above mean" requirement.
        abs_amount = df_feat["amount"].abs()
        
        # 1. Z-score within category (outlier detection)
        if "category" in df_feat.columns:
            df_feat["amount_zscore_in_category"] = abs_amount.groupby(df_feat["category"]).transform(
                lambda x: (x - x.mean()) / x.std()
            ).fillna(0.0)
        else:
            df_feat["amount_zscore_in_category"] = 0.0
            
        # 4. High-value transaction flag (> 2 std devs above category mean)
        df_feat["is_high_value"] = df_feat["amount_zscore_in_category"] > 2.0
        
        # Sort by date for rolling time-window calculations
        if "date" in df_feat.columns:
            df_feat = df_feat.sort_values(by="date")
            
            # 2. Rolling 30-day average spend
            # Use a time-aware rolling window by temporarily setting the date as index
            rolling_avg = (
                df_feat.set_index("date")["amount"]
                .abs()
                .rolling("30D")
                .mean()
            )
            df_feat["rolling_30d_avg_spend"] = rolling_avg.values
            
            # 3. Spend velocity (delta of rolling avg over time)
            df_feat["spend_velocity"] = df_feat["rolling_30d_avg_spend"].diff().fillna(0.0)
        else:
            df_feat["rolling_30d_avg_spend"] = np.nan
            df_feat["spend_velocity"] = np.nan

        return df_feat
