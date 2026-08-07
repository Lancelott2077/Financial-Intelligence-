"""
processing/normaliser.py — Transaction data normaliser.

Standardises a raw DataFrame from CSVParser into a uniform schema:
- Parses and standardises date columns.
- Converts amounts to a consistent signed float (debit = negative).
- Strips and cleans description text.
- Fills missing fields with sensible defaults.
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
        """
        # 1. Create a working copy
        df_norm = df.copy()

        # 2. Extract column references safely
        date_col = column_map.get("date")
        desc_col = column_map.get("description")
        amount_col = column_map.get("amount")
        debit_col = column_map.get("debit")
        credit_col = column_map.get("credit")

        # Ensure we have the minimum required columns for normalisation
        if not date_col or not desc_col or (not amount_col and not (debit_col or credit_col)):
            raise ValueError("Incomplete column map provided to Normaliser.")

        # 3. Rename directly mappable columns
        rename_dict = {date_col: "date", desc_col: "description"}
        if amount_col:
            rename_dict[amount_col] = "amount"
            
        df_norm = df_norm.rename(columns=rename_dict)

        # 4. Clean and parse description
        df_norm["description"] = (
            df_norm["description"]
            .astype(str)
            .str.replace(r'\s+', ' ', regex=True)  # Collapse internal whitespace
            .str.strip()
        )

        # 5. Parse dates robustly
        # dayfirst=True is preferred for IN/UK formats. 
        # errors='coerce' turns unparseable dates into NaT
        df_norm["date"] = pd.to_datetime(df_norm["date"], dayfirst=True, errors="coerce")

        # 6. Parse and sign amounts
        def clean_numeric_series(s: pd.Series) -> pd.Series:
            """Cleans currency strings into numeric series, coercing errors to NaN."""
            s_str = s.astype(str).str.strip()
            # Convert accounting format (100) to -100
            s_str = s_str.str.replace(r'^\((.*)\)$', r'-\1', regex=True)
            # Remove all characters except digits, minus, and decimal point
            s_str = s_str.str.replace(r'[^\d\.\-]', '', regex=True)
            # Convert empty or nan strings to pd.NA
            s_str = s_str.replace({'': pd.NA, 'nan': pd.NA, 'None': pd.NA})
            return pd.to_numeric(s_str, errors="coerce")

        if amount_col:
            # We already renamed it to "amount"
            df_norm["amount"] = clean_numeric_series(df_norm["amount"])
        else:
            # Handle split debit/credit columns
            debits = pd.Series(0.0, index=df_norm.index)
            credits = pd.Series(0.0, index=df_norm.index)
            
            if debit_col and debit_col in df_norm.columns:
                debits = clean_numeric_series(df_norm[debit_col]).fillna(0.0)
            if credit_col and credit_col in df_norm.columns:
                credits = clean_numeric_series(df_norm[credit_col]).fillna(0.0)
                
            # Debits are negative, credits are positive
            df_norm["amount"] = credits - debits

        # 7. Drop rows missing critical data (invalid date or amount)
        df_norm = df_norm.dropna(subset=["date", "amount"])

        # 8. Add default currency if not present
        if "currency" not in df_norm.columns:
            df_norm["currency"] = "INR"

        # 9. Return only the standard schema columns
        return df_norm[self.STANDARD_COLUMNS].copy()
