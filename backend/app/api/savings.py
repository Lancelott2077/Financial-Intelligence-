"""
api/savings.py — Savings Opportunities endpoint.

Returns ranked savings recommendations derived from the behaviour
analysis and spending patterns.

TODO: Implement via SavingsService.
TODO: Rank recommendations by estimated monthly impact.
"""

from __future__ import annotations

from fastapi import APIRouter
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
    """
    opportunities = [
        {
            "id": 1,
            "title": "Reduce dining out",
            "category": "food_and_dining",
            "current_monthly_spend": 720.0,
            "suggested_monthly_spend": 520.0,
            "estimated_monthly_saving": 200.0,
            "difficulty": "medium",
            "rationale": "Cut discretionary dining by 2–3 meals per month.",
        },
        {
            "id": 2,
            "title": "Trim shopping budget",
            "category": "shopping",
            "current_monthly_spend": 560.0,
            "suggested_monthly_spend": 380.0,
            "estimated_monthly_saving": 180.0,
            "difficulty": "medium",
            "rationale": "Avoid impulse purchases by setting a clear shopping limit.",
        },
        {
            "id": 3,
            "title": "Optimize transport costs",
            "category": "transport",
            "current_monthly_spend": 210.0,
            "suggested_monthly_spend": 150.0,
            "estimated_monthly_saving": 60.0,
            "difficulty": "low",
            "rationale": "Use rideshare discounts and more public transport trips.",
        },
        {
            "id": 4,
            "title": "Review utility plans",
            "category": "utilities",
            "current_monthly_spend": 320.0,
            "suggested_monthly_spend": 260.0,
            "estimated_monthly_saving": 60.0,
            "difficulty": "low",
            "rationale": "Switch to a better electricity or broadband plan.",
        },
    ]
    total_saving = sum(item["estimated_monthly_saving"] for item in opportunities)
    return {
        "session_id": session_id,
        "total_potential_monthly_saving": round(total_saving, 2),
        "opportunities": opportunities,
    }
