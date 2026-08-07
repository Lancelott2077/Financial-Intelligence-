"""schemas/savings.py — Savings Opportunities Pydantic schemas."""

from __future__ import annotations

from typing import List
from pydantic import Field
from app.schemas.common import BaseResponse, SeverityLevel


class SavingOpportunity(BaseResponse):
    """A single ranked savings opportunity."""

    id: int
    title: str
    category: str
    current_monthly_spend: float
    suggested_monthly_spend: float
    estimated_monthly_saving: float
    difficulty: SeverityLevel = SeverityLevel.MEDIUM
    rationale: str


class SavingsResponse(BaseResponse):
    """
    Ranked list of savings opportunities for an upload session.

    TODO: Populate from SavingsService.get_opportunities().
    """

    session_id: str
    total_potential_monthly_saving: float = 0.0
    opportunities: List[SavingOpportunity] = Field(default_factory=list)
