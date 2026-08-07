"""schemas/plan.py — Action Plan Pydantic schemas."""

from __future__ import annotations

from typing import List
from pydantic import Field
from app.schemas.common import BaseResponse, SeverityLevel


class PlanItem(BaseResponse):
    """A single item in the personalised action plan."""

    id: int
    title: str
    description: str
    estimated_monthly_saving: float
    priority: SeverityLevel
    target_date: str | None = None
    status: str = "pending"
    linked_behaviour_id: int | None = None


class PlanResponse(BaseResponse):
    """
    Complete action plan for an upload session.

    TODO: Populate from PlanService.generate_plan().
    """

    session_id: str
    items: List[PlanItem] = Field(default_factory=list)
    total_estimated_monthly_saving: float = 0.0
