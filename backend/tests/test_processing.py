"""
tests/test_processing.py — Data processing pipeline tests.

TODO: Implement tests for CSVParser, Normaliser, Categoriser.
"""

import pytest


class TestCSVParser:
    """Tests for the CSV parser module."""

    def test_parse_valid_csv(self):
        """TODO: Test parsing a valid bank statement CSV."""
        pytest.skip("CSVParser not yet implemented.")

    def test_missing_required_columns_raises(self):
        """TODO: Test that missing required columns raise ValueError."""
        pytest.skip("CSVParser not yet implemented.")


class TestNormaliser:
    """Tests for the transaction normaliser."""

    def test_date_parsing(self):
        """TODO: Test date parsing in multiple formats."""
        pytest.skip("Normaliser not yet implemented.")

    def test_amount_sign_normalisation(self):
        """TODO: Test debit/credit sign convention normalisation."""
        pytest.skip("Normaliser not yet implemented.")


class TestCategoriser:
    """Tests for the transaction categoriser."""

    def test_keyword_categorisation(self):
        """TODO: Test keyword-based category assignment."""
        pytest.skip("Categoriser not yet implemented.")
