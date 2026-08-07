"""
api/plan.py — Action Plan endpoint.

Returns a prioritised, time-bound action plan generated from
detected behaviours and savings opportunities.

TODO: Implement via PlanService.
TODO: Support plan item status updates (mark complete / skip).
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException, status
from app.schemas.plan import PlanResponse

router = APIRouter()


@router.get(
    "/{session_id}",
    response_model=PlanResponse,
    summary="Get the personalised action plan for a session",
)
async def get_plan(session_id: str) -> PlanResponse:
    """
    Return a prioritised action plan for the given session.

    TODO: Validate session_id exists.
    TODO: Call PlanService.generate_plan(session_id).
    TODO: Return populated PlanResponse.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Plan endpoint not yet implemented.",
    )
