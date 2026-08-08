"""
api/plan.py — Action Plan endpoint.

Returns a prioritised, time-bound action plan generated from
detected behaviours and savings opportunities.

TODO: Implement via PlanService.
TODO: Support plan item status updates (mark complete / skip).
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.models.plan import ActionPlanItem
from app.schemas.plan import PlanResponse, PlanItem
from app.schemas.common import PlanItemStatus, SeverityLevel

router = APIRouter()


@router.get(
    "/{session_id}",
    response_model=PlanResponse,
    summary="Get the personalised action plan for a session",
)
async def get_plan(session_id: str, db: Session = Depends(get_db)) -> PlanResponse:
    """
    Return a prioritised action plan for the given session.
    """
    db_items = db.query(ActionPlanItem).filter(
        ActionPlanItem.session_id == session_id
    ).all()

    items = []
    for item in db_items:
        try:
            priority_enum = SeverityLevel(item.priority)
        except ValueError:
            priority_enum = SeverityLevel.MEDIUM

        try:
            status_enum = PlanItemStatus(item.status)
        except ValueError:
            status_enum = PlanItemStatus.PENDING

        items.append(
            PlanItem(
                id=item.id,
                title=item.title,
                description=item.description or "",
                estimated_monthly_saving=item.estimated_saving,
                priority=priority_enum,
                target_date=item.target_date.isoformat() if item.target_date else None,
                status=status_enum,
                linked_behaviour_id=item.behaviour_id,
                linked_bias_type=None,
            )
        )

    total_saving = sum(i.estimated_monthly_saving for i in items)

    return PlanResponse(
        session_id=session_id,
        items=items,
        total_estimated_monthly_saving=round(total_saving, 2),
    )
