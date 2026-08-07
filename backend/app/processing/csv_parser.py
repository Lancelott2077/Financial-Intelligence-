"""
processing/csv_parser.py — Raw CSV file reader and validator.

Reads the uploaded CSV file into a pandas DataFrame and validates
that the required columns are present.
"""

from __future__ import annotations

from pathlib import Path
import pandas as pd


class CSVParser:
    """Reads and performs initial validation of bank transaction CSV files."""

    SUPPORTED_DATE_COLUMNS: list[str] = ["date", "transaction date", "posting date", "txn date", "date of transaction"]
    SUPPORTED_AMOUNT_COLUMNS: list[str] = ["amount", "value", "transaction amount"]
    SUPPORTED_DEBIT_COLUMNS: list[str] = ["debit", "withdrawal"]
    SUPPORTED_CREDIT_COLUMNS: list[str] = ["credit", "deposit"]
    SUPPORTED_DESCRIPTION_COLUMNS: list[str] = ["description", "narration", "particulars", "memo", "details", "transaction details"]

    def parse(self, file_path: Path) -> pd.DataFrame:
        """
        Read a CSV file and return a raw DataFrame.

        Args:
            file_path: Path to the uploaded CSV file.

        Returns:
            Raw pandas DataFrame with at least the detected columns.

        Raises:
            ValueError: If the file cannot be parsed or required columns are missing.
        """
        if not file_path.exists():
            raise ValueError(f"CSV file not found: {file_path}")

        encodings_to_try = ["utf-8-sig", "utf-8", "latin-1", "cp1252"]
        delimiters_to_try = [",", ";", "\t", "|"]
        
        df = None
        for encoding in encodings_to_try:
            for delimiter in delimiters_to_try:
                try:
                    df_attempt = pd.read_csv(
                        file_path, 
                        encoding=encoding, 
                        sep=delimiter, 
                        dtype=str  # Read everything as string initially to avoid parsing errors
                    )
                    
                    if not df_attempt.empty and len(df_attempt.columns) > 1:
                        df = df_attempt
                        break
                except (UnicodeDecodeError, pd.errors.ParserError, ValueError):
                    # These are expected errors when trying wrong encodings or delimiters.
                    continue
            if df is not None:
                break
                
        if df is None or df.empty:
            raise ValueError("Failed to parse CSV file. Ensure it is a valid text file with a supported delimiter.")
            
        # Standardise column names: lower case and strip whitespace
        df.columns = df.columns.astype(str).str.strip().str.lower()
        
        return df

    def detect_columns(self, df: pd.DataFrame) -> dict[str, str]:
        """
        Map raw column names to standard field names.

        Returns:
            Dict mapping standard_name → detected_column_name.
        """
        column_map: dict[str, str] = {}
        df_columns = df.columns.tolist()

        def find_match(supported_list: list[str]) -> str | None:
            # 1. Exact match
            for col in df_columns:
                if col in supported_list:
                    return col
            
            # 2. Substring match
            for col in df_columns:
                for supported in supported_list:
                    if supported in col:
                        return col
            return None

        date_col = find_match(self.SUPPORTED_DATE_COLUMNS)
        if not date_col:
            raise ValueError(f"Could not detect a valid 'date' column. Expected one of: {self.SUPPORTED_DATE_COLUMNS}")
        column_map["date"] = date_col

        desc_col = find_match(self.SUPPORTED_DESCRIPTION_COLUMNS)
        if not desc_col:
            raise ValueError(f"Could not detect a valid 'description' column. Expected one of: {self.SUPPORTED_DESCRIPTION_COLUMNS}")
        column_map["description"] = desc_col

        # Handle amounts: try combined amount column first, then fallback to separate debit/credit columns
        amount_col = find_match(self.SUPPORTED_AMOUNT_COLUMNS)
        if amount_col:
            column_map["amount"] = amount_col
        else:
            debit_col = find_match(self.SUPPORTED_DEBIT_COLUMNS)
            credit_col = find_match(self.SUPPORTED_CREDIT_COLUMNS)
            
            if not debit_col and not credit_col:
                raise ValueError(
                    f"Could not detect a valid 'amount', or 'debit'/'credit' columns. "
                    f"Expected one of {self.SUPPORTED_AMOUNT_COLUMNS} OR {self.SUPPORTED_DEBIT_COLUMNS}/{self.SUPPORTED_CREDIT_COLUMNS}."
                )
            
            if debit_col:
                column_map["debit"] = debit_col
            if credit_col:
                column_map["credit"] = credit_col

        return column_map
