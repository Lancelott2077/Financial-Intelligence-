"""
schemas/savings.py — Savings Opportunities API schemas.

Object ownership:
    SavingOpportunity   Owned by: SavingsService (app/services/savings_service.py)
                        Consumer: SavingsResponse, Frontend Savings page
    SavingsResponse     Owned by: API layer (app/api/savings.py)
                        Consumer: Frontend Savings Opportunities page
"""

from __future__ import annotations

from typing import List
from pydantic import Field
from app.schemas.common import BaseResponse, SeverityLevel, SpendingCategory


class SavingOpportunity(BaseResponse):
    """
    A single ranked savings opportunity.

    Fields:
        id                      Database ID (or generated rank index).
        title                   Short human-readable title.
        category                Spending category this opportunity targets.
        current_monthly_spend   Avg monthly spend in this category (from data).
        suggested_monthly_spend Suggested new target monthly spend.
        estimated_monthly_saving Difference: current minus suggested.
        difficulty              How hard this change is: low | medium | high.
        rationale               Explanation of why this opportunity was identified.
    """

    id: int
    title: str = Field(description="Short human-readable title.")
    category: SpendingCategory = Field(description="Targeted spending category.")
    current_monthly_spend: float = Field(
        ge=0.0, description="Current avg monthly spend in this category."
    )
    suggested_monthly_spend: float = Field(
        ge=0.0, description="Suggested new monthly spend target."
    )
    estimated_monthly_saving: float = Field(
        ge=0.0, description="Projected monthly saving (current minus suggested)."
    )
    difficulty: SeverityLevel = Field(
        default=SeverityLevel.MEDIUM,
        description="Behaviour change difficulty: low | medium | high.",
    )
    rationale: str = Field(description="Why this opportunity was identified.")


class SavingsResponse(BaseResponse):
    """
    Ranked list of savings opportunities for an upload session.

    Fields:
        session_id                      UUID of the upload session.
        total_potential_monthly_saving  Sum of all opportunity estimated_monthly_saving.
        opportunities                   Ranked list, highest saving first.
    """

    session_id: str
    total_potential_monthly_saving: float = Field(
        default=0.0,
        description="Sum of all opportunity estimated_monthly_saving values.",
    )
    opportunities: List[SavingOpportunity] = Field(
        default_factory=list,
        description="Ranked savings opportunities, highest saving first.",
    )
