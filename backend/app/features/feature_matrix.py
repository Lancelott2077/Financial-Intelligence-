"""
features/feature_matrix.py — Unified feature matrix assembler.

Chains all individual feature extractors and returns a single
enriched DataFrame ready for the behaviour detection layer.
"""

from __future__ import annotations

import pandas as pd
from loguru import logger

from app.features.temporal_features import TemporalFeatureExtractor
from app.features.spending_features import SpendingFeatureExtractor
from app.features.merchant_features import MerchantFeatureExtractor
from app.features.category_features import CategoryFeatureExtractor


class FeatureMatrix:
    """Assembles a unified feature matrix from all extractors."""

    EXPECTED_FEATURES = {
        "day_of_week",
        "is_weekend",
        "days_from_payday",
        "days_since_last_purchase_in_category",
        "amount_zscore_in_category",
        "rolling_30d_avg_spend",
        "spend_velocity",
        "is_high_value",
        "merchant_visit_frequency",
        "merchant_avg_spend",
        "merchant_loyalty_score",
        "category_monthly_share",
        "category_mom_drift",
        "category_rank",
    }

    def __init__(self) -> None:
        self._temporal = TemporalFeatureExtractor()
        self._spending = SpendingFeatureExtractor()
        self._merchant = MerchantFeatureExtractor()
        self._category = CategoryFeatureExtractor()

    def build(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Run all extractors and return the enriched feature DataFrame.

        Args:
            df: Normalised and categorised transaction DataFrame.

        Returns:
            DataFrame with all feature columns appended.
        """
        if df.empty:
            logger.warning("FeatureMatrix received an empty DataFrame. Returning empty schema.")
            df_empty = df.copy()
            for col in self.EXPECTED_FEATURES:
                if col not in df_empty.columns:
                    df_empty[col] = pd.Series(dtype="float64")
            return df_empty

        try:
            initial_len = len(df)
            df_feat = df.copy()

            # Handle feature column naming conflicts with incoming DataFrame
            conflicts = set(df_feat.columns).intersection(self.EXPECTED_FEATURES)
            if conflicts:
                logger.info(f"Dropping pre-existing conflicting columns: {conflicts}")
                df_feat = df_feat.drop(columns=list(conflicts))

            logger.info(f"Starting feature assembly pipeline for {initial_len} transactions.")
            
            # Chain extractor calls sequentially
            df_feat = self._temporal.extract(df_feat)
            df_feat = self._spending.extract(df_feat)
            df_feat = self._merchant.extract(df_feat)
            df_feat = self._category.extract(df_feat)

            # Validate row count preservation
            if len(df_feat) != initial_len:
                raise RuntimeError(
                    f"Row count mismatch during assembly: started with {initial_len}, "
                    f"ended with {len(df_feat)}."
                )

            # Validate output schema completeness (fail-fast)
            missing_features = self.EXPECTED_FEATURES - set(df_feat.columns)
            if missing_features:
                raise RuntimeError(
                    f"Feature extraction failed to produce required columns: {missing_features}. "
                    "Downstream detectors cannot proceed."
                )

            # Log feature counts for debugging
            logger.info(
                f"Feature assembly complete. Successfully generated {len(self.EXPECTED_FEATURES)} "
                f"features across {len(df_feat)} transactions."
            )

            return df_feat

        except Exception as e:
            logger.error(f"Feature assembly pipeline failed: {e}", exc_info=True)
            # Re-raise as a clear RuntimeError to be caught by AnalysisPipeline
            raise RuntimeError(f"Feature assembly pipeline failed: {e}") from e
