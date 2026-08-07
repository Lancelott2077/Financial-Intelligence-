"""
schemas/plan.py — Action Plan API schemas.

Object ownership:
    PlanItem        Owned by: PlanService (app/services/plan_service.py)
                    Consumer: PlanResponse, Frontend Action Plan page
    PlanResponse    Owned by: API layer (app/api/plan.py)
                    Consumer: Frontend Action Plan page
"""

from __future__ import annotations

from typing import List
from pydantic import Field
from app.schemas.common import BaseResponse, SeverityLevel, PlanItemStatus, BiasType


class PlanItem(BaseResponse):
    """
    A single item in the personalised action plan.

    Fields:
        id                      Database ID of the ActionPlanItem row.
        title                   Short title of the action.
        description             Detailed description and rationale.
        estimated_monthly_saving Projected monthly saving in session currency.
        priority                Priority level: low | medium | high.
        target_date             Target completion date (YYYY-MM-DD), or None.
        status                  Lifecycle status: pending | in_progress | completed | skipped.
        linked_behaviour_id     DB id of the DetectedBehaviour that triggered this item, or None.
        linked_bias_type        BiasType that triggered this item, or None.
    """

    id: int
    title: str = Field(description="Short action title.")
    description: str = Field(description="Full description and rationale.")
    estimated_monthly_saving: float = Field(
        ge=0.0, description="Projected monthly saving in session currency."
    )
    priority: SeverityLevel = Field(description="Priority: low | medium | high.")
    target_date: str | None = Field(
        default=None, description="Target completion date (YYYY-MM-DD)."
    )
    status: PlanItemStatus = Field(
        default=PlanItemStatus.PENDING,
        description="Lifecycle status: pending | in_progress | completed | skipped.",
    )
    linked_behaviour_id: int | None = Field(
        default=None, description="DB id of the triggering DetectedBehaviour, if any."
    )
    linked_bias_type: BiasType | None = Field(
        default=None, description="BiasType that triggered this item, if any."
    )


class PlanResponse(BaseResponse):
    """
    Complete action plan for an upload session.

    Fields:
        session_id                      UUID of the upload session.
        items                           All plan items, sorted by priority descending.
        total_estimated_monthly_saving  Sum of estimated_monthly_saving across all items.
    """

    session_id: str
    items: List[PlanItem] = Field(
        default_factory=list,
        description="Plan items, sorted by priority descending.",
    )
    total_estimated_monthly_saving: float = Field(
        default=0.0,
        description="Sum of all estimated_monthly_saving values.",
    )
