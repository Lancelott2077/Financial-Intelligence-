"""utils/date_utils.py — Date parsing, formatting, and range helpers."""

from __future__ import annotations

from datetime import date, datetime
from typing import List, Tuple


def parse_date(value: str) -> date:
    """
    Parse a date string in multiple common formats.

    Supported formats: YYYY-MM-DD, DD/MM/YYYY, MM/DD/YYYY, DD-MM-YYYY.

    TODO: Implement multi-format date parsing using dateutil.
    """
    raise NotImplementedError("parse_date not implemented.")


def format_month_label(year: int, month: int) -> str:
    """
    Format a year/month pair as a 'YYYY-MM' label string.

    TODO: Implement formatting.
    """
    raise NotImplementedError("format_month_label not implemented.")


def get_date_range(dates: List[date]) -> Tuple[date, date]:
    """
    Return the min and max dates from a list.

    TODO: Implement min/max extraction.
    """
    raise NotImplementedError("get_date_range not implemented.")
