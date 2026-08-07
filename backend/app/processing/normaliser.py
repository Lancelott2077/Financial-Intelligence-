"""
processing/normaliser.py — Transaction data normaliser.

Standardises a raw DataFrame from CSVParser into a uniform schema:
- Parses and standardises date columns.
- Converts amounts to a consistent signed float (debit = negative).
- Strips and cleans description text.
- Fills missing fields with sensible defaults.

TODO: Implement date parsing with multiple format support.
TODO: Implement amount sign normalisation (debit/credit columns → signed).
TODO: Implement description text cleaning (strip, lower, remove special chars).
"""

from __future__ import annotations

import pandas as pd


class Normaliser:
    """Normalises raw transaction DataFrames into a standard schema."""

    STANDARD_COLUMNS = ["date", "description", "amount", "currency"]

    def normalise(self, df: pd.DataFrame, column_map: dict[str, str]) -> pd.DataFrame:
        """
        Apply normalisation transforms to a raw DataFrame.

        Args:
            df:             Raw DataFrame from CSVParser.
            column_map:     Mapping from standard names to detected column names.

        Returns:
            Normalised DataFrame with standard columns.

        TODO: Rename detected columns to standard names.
        TODO: Parse date column to datetime.date.
        TODO: Normalise amount sign convention.
        TODO: Clean description text.
        TODO: Drop rows with null date or amount.
        """
        raise NotImplementedError("Normaliser.normalise not implemented.")
