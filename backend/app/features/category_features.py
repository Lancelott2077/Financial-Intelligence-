"""
features/category_features.py — Category share and drift feature extractor.

Computes features at the spending category level:
- Category share of total monthly spend
- Month-over-month category spend drift
- Budget adherence ratio (if budget data available)
"""

from __future__ import annotations

import pandas as pd
import numpy as np


class CategoryFeatureExtractor:
    """Extracts category-level share and drift features."""

    def extract(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Add category-level feature columns to the transaction DataFrame.

        Args:
            df: Normalised DataFrame with 'category', 'amount', 'date' columns.

        Returns:
            DataFrame with additional category feature columns.
        """
        # Ensure required columns exist
        if df.empty or not {"category", "amount", "date"}.issubset(df.columns):
            return df
            
        df_feat = df.copy()
        
        # We work with absolute amounts to uniformly treat both large expenses and large incomes 
        abs_amount = df_feat["amount"].abs()
        
        # Create a temporary period column for discrete calendar month grouping
        df_feat["_year_month"] = df_feat["date"].dt.to_period("M")
        
        # Calculate base aggregations
        cat_monthly = abs_amount.groupby([df_feat["category"], df_feat["_year_month"]]).sum()
        monthly_total = abs_amount.groupby(df_feat["_year_month"]).sum()
        
        # 1. Category Monthly Share (% of total monthly spend)
        # Divide category spend by total month spend, mapping across the _year_month index level
        cat_monthly_share = cat_monthly.div(monthly_total, level="_year_month").fillna(0.0)
        
        # 2. Category Rank (rank of category by spend per month)
        # Rank within each month. Highest spend = rank 1. Ties get the same minimum rank.
        cat_rank = cat_monthly.groupby(level="_year_month").rank(method="min", ascending=False)
        
        # 3. Category MoM Drift (month-over-month % change in category spend)
        # Unstack to force a complete grid of all months (filling missing with 0.0)
        cat_monthly_unstacked = cat_monthly.unstack(level="_year_month", fill_value=0.0)
        
        # Calculate percentage change along the month axis
        mom_drift_unstacked = cat_monthly_unstacked.pct_change(axis=1)
        
        # Stack back to multi-index, ensuring we don't drop NaNs to maintain alignment
        cat_mom_drift = mom_drift_unstacked.stack()
        
        # Replace mathematical inf/-inf (from zero-baseline division) with NaN
        cat_mom_drift = cat_mom_drift.replace([np.inf, -np.inf], np.nan)
        
        # Combine all computed features into a single summary DataFrame
        summary_df = pd.DataFrame({
            "category_monthly_share": cat_monthly_share,
            "category_rank": cat_rank,
            "category_mom_drift": cat_mom_drift
        })
        
        # Join summary metrics back to the main DataFrame
        # df.join strictly preserves the original row order and index of df_feat
        df_feat = df_feat.join(summary_df, on=["category", "_year_month"])
        
        # Clean up temporary column
        df_feat = df_feat.drop(columns=["_year_month"])
        
        return df_feat
