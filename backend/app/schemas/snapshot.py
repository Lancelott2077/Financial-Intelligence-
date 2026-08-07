"""schemas/snapshot.py — Financial Snapshot Pydantic schemas."""

from __future__ import annotations

from typing import Dict, List
from pydantic import Field
from app.schemas.common import BaseResponse


class CategoryBreakdown(BaseResponse):
    """Spending breakdown for a single category."""

    category: str
    total: float
    percentage: float
    transaction_count: int


class MonthlyTrend(BaseResponse):
    """Income and expense totals for a single month."""

    month: str  # e.g. "2024-01"
    income: float
    expenses: float
    net: float


class SnapshotResponse(BaseResponse):
    """
    Aggregated financial snapshot for an upload session.

    TODO: Populate from SnapshotService.build_snapshot().
    """

    session_id: str
    total_income: float = Field(default=0.0, description="Total credits.")
    total_expenses: float = Field(default=0.0, description="Total debits.")
    net_savings: float = Field(default=0.0, description="Income minus expenses.")
    savings_rate: float = Field(default=0.0, description="Savings as % of income.")
    transaction_count: int = Field(default=0)
    date_range_start: str | None = None
    date_range_end: str | None = None
    category_breakdown: List[CategoryBreakdown] = Field(default_factory=list)
    monthly_trends: List[MonthlyTrend] = Field(default_factory=list)
