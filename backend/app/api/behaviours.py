"""
api/behaviours.py — Detected Behaviours endpoint.

Returns a list of identified cognitive / behavioural biases
(e.g., present bias, loss aversion, anchoring) with supporting evidence.

TODO: Implement via BehaviourService.
TODO: Support filtering by bias category.
"""

from __future__ import annotations

from fastapi import APIRouter
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
    """
    behaviours = [
        {
            "id": 1,
            "bias_type": "present_bias",
            "display_name": "Present Bias",
            "confidence": 0.82,
            "severity": "medium",
            "detected": True,
            "summary": "High-value discretionary purchases clustered near payday suggest present bias.",
            "evidence": [
                {
                    "transaction_id": 101,
                    "date": "2026-07-29",
                    "description": "Weekend dining at Bistro Cafe",
                    "amount": -115.45,
                    "category": "food_and_dining",
                    "explanation": "High-value weekend dining purchase close to payday.",
                },
                {
                    "transaction_id": 102,
                    "date": "2026-07-27",
                    "description": "Movie tickets and snacks",
                    "amount": -62.30,
                    "category": "entertainment",
                    "explanation": "Impulse entertainment spend after income deposit.",
                },
            ],
        },
        {
            "id": 2,
            "bias_type": "loss_aversion",
            "display_name": "Loss Aversion",
            "confidence": 0.74,
            "severity": "medium",
            "detected": True,
            "summary": "Recurring subscription and insurance payments suggest reluctance to reduce recurring costs.",
            "evidence": [
                {
                    "transaction_id": 213,
                    "date": "2026-07-05",
                    "description": "Health insurance premium",
                    "amount": -180.00,
                    "category": "healthcare",
                    "explanation": "Fixed insurance payment retained despite high monthly spend.",
                },
                {
                    "transaction_id": 214,
                    "date": "2026-07-12",
                    "description": "Streaming subscription renewal",
                    "amount": -24.99,
                    "category": "entertainment",
                    "explanation": "Ongoing subscription spend with low perceived flexibility.",
                },
            ],
        },
        {
            "id": 3,
            "bias_type": "mental_accounting",
            "display_name": "Mental Accounting",
            "confidence": 0.68,
            "severity": "medium",
            "detected": True,
            "summary": "Luxury spending spikes appear tied to bonus-like income deposits.",
            "evidence": [
                {
                    "transaction_id": 321,
                    "date": "2026-07-15",
                    "description": "Luxury goods purchase",
                    "amount": -320.00,
                    "category": "shopping",
                    "explanation": "High discretionary spend following salary credit.",
                },
                {
                    "transaction_id": 322,
                    "date": "2026-07-16",
                    "description": "Hotel booking for leisure trip",
                    "amount": -178.50,
                    "category": "travel",
                    "explanation": "Luxury travel booking after income arrival indicates siloed spending.",
                },
            ],
        },
    ]
    return {
        "session_id": session_id,
        "behaviours": behaviours,
        "total_count": len(behaviours),
    }
