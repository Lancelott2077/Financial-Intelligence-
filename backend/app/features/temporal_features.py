"""
features/temporal_features.py — Time-based feature extractor.

Computes features related to when transactions occur:
- Day of week (0=Monday, 6=Sunday)
- Is weekend flag
- Is payday proximity flag
- Time since last transaction in same category
"""

from __future__ import annotations

import pandas as pd
import numpy as np


class TemporalFeatureExtractor:
    """Extracts time-based features from transaction data."""

    def extract(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Add temporal feature columns to the transaction DataFrame.

        Args:
            df: Normalised DataFrame with a 'date' column.

        Returns:
            DataFrame with additional temporal feature columns.
        """
        if df.empty or "date" not in df.columns:
            return df
            
        # Create a working copy
        df_feat = df.copy()

        # 1. Day of week (0=Monday, 6=Sunday)
        df_feat["day_of_week"] = df_feat["date"].dt.dayofweek

        # 2. Is weekend boolean column
        df_feat["is_weekend"] = df_feat["day_of_week"] >= 5
        
        # Sort by date for sequential calculations (retains original index for tracking)
        df_sorted = df_feat.sort_values(by="date")

        # 3. Days from payday (detect payday from income transactions i.e. amount > 0)
        if "amount" in df_sorted.columns:
            # Create a Series of payday dates, NaN where amount <= 0
            paydays = df_sorted["date"].where(df_sorted["amount"] > 0)
            # Forward fill to propagate the most recent payday to subsequent rows
            last_payday = paydays.ffill()
            # Calculate difference in days. Aligns automatically by index.
            df_feat["days_from_payday"] = (df_sorted["date"] - last_payday).dt.days
        else:
            df_feat["days_from_payday"] = np.nan

        # 4. Days since last purchase in category
        if "category" in df_sorted.columns:
            # Group by category on the sorted dataframe, get the previous date
            prev_date = df_sorted.groupby("category")["date"].shift(1)
            df_feat["days_since_last_purchase_in_category"] = (df_sorted["date"] - prev_date).dt.days
        else:
            df_feat["days_since_last_purchase_in_category"] = np.nan

        return df_feat
