"""
processing/categoriser.py — Transaction spending category classifier.

Assigns a spending category to each transaction using keyword rules
and/or a Gemini AI call for ambiguous transactions.

TODO: Implement keyword-based rule classifier (fast path).
TODO: Implement Gemini-based classifier for unmatched transactions (slow path).
TODO: Define category taxonomy.
"""

from __future__ import annotations

import pandas as pd


# TODO: Define the full category taxonomy.
CATEGORIES = [
    "food_and_dining",
    "groceries",
    "transport",
    "entertainment",
    "utilities",
    "healthcare",
    "shopping",
    "education",
    "travel",
    "income",
    "transfer",
    "other",
]


class Categoriser:
    """Classifies transactions into spending categories."""

    def categorise(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Add a 'category' column to the normalised DataFrame.

        Args:
            df: Normalised DataFrame (must have 'description' column).

        Returns:
            DataFrame with 'category' column populated.

        TODO: Apply keyword rule classifier first.
        TODO: For unmatched rows, call Gemini API in batches.
        TODO: Cache Gemini results to reduce API calls.
        """
        raise NotImplementedError("Categoriser.categorise not implemented.")
