"""
api/savings.py — Savings Opportunities endpoint.

Returns ranked savings recommendations derived from the behaviour
analysis and spending patterns.

TODO: Implement via SavingsService.
TODO: Rank recommendations by estimated monthly impact.
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException, status
from app.schemas.savings import SavingsResponse

router = APIRouter()


@router.get(
    "/{session_id}",
    response_model=SavingsResponse,
    summary="Get savings opportunities for a session",
)
async def get_savings(session_id: str) -> SavingsResponse:
    """
    Return ranked savings opportunities for the given session.

    TODO: Validate session_id exists.
    TODO: Call SavingsService.get_opportunities(session_id).
    TODO: Return populated SavingsResponse.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Savings endpoint not yet implemented.",
    )
