"""
api/snapshot.py — Financial Snapshot endpoint.

Returns an aggregated summary of processed transactions for a session:
total income, total expenses, net savings, category breakdown, and
monthly trends.

TODO: Implement snapshot aggregation via SnapshotService.
TODO: Add query params for date range filtering.
"""

from __future__ import annotations

from fastapi import APIRouter
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
    """
    return {
        "session_id": session_id,
        "total_income": 12450.0,
        "total_expenses": 8320.0,
        "net_savings": 4130.0,
        "savings_rate": 33.2,
        "transaction_count": 48,
        "date_range_start": "2026-07-01",
        "date_range_end": "2026-07-31",
        "category_breakdown": [
            {"category": "food_and_dining", "total": 2750.0, "percentage": 33.1, "transaction_count": 12},
            {"category": "shopping", "total": 1480.0, "percentage": 17.8, "transaction_count": 8},
            {"category": "transport", "total": 940.0, "percentage": 11.3, "transaction_count": 7},
            {"category": "utilities", "total": 620.0, "percentage": 7.5, "transaction_count": 4},
            {"category": "income", "total": 12450.0, "percentage": 100.0, "transaction_count": 5},
        ],
        "monthly_trends": [
            {"month": "2026-05", "income": 12100.0, "expenses": 7900.0, "net": 4200.0},
            {"month": "2026-06", "income": 12300.0, "expenses": 8200.0, "net": 4100.0},
            {"month": "2026-07", "income": 12450.0, "expenses": 8320.0, "net": 4130.0},
        ],
    }
