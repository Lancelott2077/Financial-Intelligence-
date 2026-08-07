"""
processing/csv_parser.py — Raw CSV file reader and validator.

Reads the uploaded CSV file into a pandas DataFrame and validates
that the required columns are present.

TODO: Implement column detection for multiple bank CSV formats.
TODO: Implement schema validation (required columns, data types).
TODO: Handle encoding issues (UTF-8, Latin-1).
TODO: Handle BOM characters common in bank exports.
"""

from __future__ import annotations

from pathlib import Path
import pandas as pd


class CSVParser:
    """Reads and performs initial validation of bank transaction CSV files."""

    # TODO: Define supported column name variants for each standard field.
    SUPPORTED_DATE_COLUMNS: list[str] = []
    SUPPORTED_AMOUNT_COLUMNS: list[str] = []
    SUPPORTED_DESCRIPTION_COLUMNS: list[str] = []

    def parse(self, file_path: Path) -> pd.DataFrame:
        """
        Read a CSV file and return a raw DataFrame.

        Args:
            file_path: Path to the uploaded CSV file.

        Returns:
            Raw pandas DataFrame with at least the detected columns.

        Raises:
            ValueError: If the file cannot be parsed or required columns are missing.

        TODO: Detect file encoding automatically.
        TODO: Try multiple delimiters (comma, semicolon, tab).
        TODO: Validate required columns exist after detection.
        """
        raise NotImplementedError("CSVParser.parse not implemented.")

    def detect_columns(self, df: pd.DataFrame) -> dict[str, str]:
        """
        Map raw column names to standard field names.

        Returns:
            Dict mapping standard_name → detected_column_name.

        TODO: Use fuzzy matching or a lookup dictionary.
        """
        raise NotImplementedError("CSVParser.detect_columns not implemented.")
