"""
api/behaviours.py — Detected Behaviours endpoint.

Returns a list of identified cognitive / behavioural biases
(e.g., present bias, loss aversion, anchoring) with supporting evidence.

TODO: Implement via BehaviourService.
TODO: Support filtering by bias category.
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException, status
from app.schemas.behaviours import BehavioursResponse

router = APIRouter()


@router.get(
    "/{session_id}",
    response_model=BehavioursResponse,
    summary="Get detected behavioural biases for a session",
)
async def get_behaviours(session_id: str) -> BehavioursResponse:
    """
    Return all detected behavioural biases for the given session.

    TODO: Validate session_id exists.
    TODO: Call BehaviourService.get_behaviours(session_id).
    TODO: Return populated BehavioursResponse.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Behaviours endpoint not yet implemented.",
    )
