"""
features/feature_matrix.py — Unified feature matrix assembler.

Chains all individual feature extractors and returns a single
enriched DataFrame ready for the behaviour detection layer.

TODO: Implement feature assembly pipeline.
TODO: Handle feature column naming conflicts.
TODO: Add feature validation / dtype enforcement.
"""

from __future__ import annotations

import pandas as pd

from app.features.temporal_features import TemporalFeatureExtractor
from app.features.spending_features import SpendingFeatureExtractor
from app.features.merchant_features import MerchantFeatureExtractor
from app.features.category_features import CategoryFeatureExtractor


class FeatureMatrix:
    """Assembles a unified feature matrix from all extractors."""

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

        TODO: Chain extractor calls sequentially.
        TODO: Log feature counts for debugging.
        TODO: Validate output schema before returning.
        """
        raise NotImplementedError("FeatureMatrix.build not implemented.")
