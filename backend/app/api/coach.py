"""
api/coach.py — AI Financial Coach conversation endpoint.

Provides a conversational interface powered by Gemini.
Accepts a user message and session context, returns an AI-generated response.

TODO: Implement via CoachService and GeminiClient.
TODO: Maintain conversation history in session.
TODO: Ground responses in session financial data.
"""

from __future__ import annotations

from fastapi import APIRouter
from app.schemas.coach import CoachRequest, CoachResponse

router = APIRouter()


@router.post(
    "/chat",
    response_model=CoachResponse,
    summary="Send a message to the AI financial coach",
)
async def chat_with_coach(request: CoachRequest) -> CoachResponse:
    """
    Process a user message and return a Gemini-powered coaching response.
    """
    reply = (
        "Thanks for your question! Based on your current spending profile, "
        "focusing on a smaller weekly dining budget and reviewing recurring subscriptions "
        "will help strengthen your financial habits."
    )
    return {
        "session_id": request.session_id,
        "reply": reply,
        "references": ["present_bias", "loss_aversion"],
    }
