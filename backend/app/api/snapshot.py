"""
api/snapshot.py — Financial Snapshot endpoint.

Returns an aggregated summary of processed transactions for a session:
total income, total expenses, net savings, category breakdown, and
monthly trends.

TODO: Implement snapshot aggregation via SnapshotService.
TODO: Add query params for date range filtering.
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException, status
from app.schemas.snapshot import SnapshotResponse

router = APIRouter()


@router.get(
    "/{session_id}",
    response_model=SnapshotResponse,
    summary="Get financial snapshot for a session",
)
async def get_snapshot(session_id: str) -> SnapshotResponse:
    """
    Return aggregated financial data for the given session.

    TODO: Validate session_id exists in database.
    TODO: Call SnapshotService.build_snapshot(session_id).
    TODO: Return populated SnapshotResponse.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Snapshot endpoint not yet implemented.",
    )
