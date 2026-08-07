"""
api/coach.py — AI Financial Coach conversation endpoint.

Provides a conversational interface powered by Gemini.
Accepts a user message and session context, returns an AI-generated response.

TODO: Implement via CoachService and GeminiClient.
TODO: Maintain conversation history in session.
TODO: Ground responses in session financial data.
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException, status
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

    TODO: Load session context (transactions, behaviours, plan).
    TODO: Build Gemini prompt from context + user message.
    TODO: Call GeminiClient.generate(prompt).
    TODO: Return structured CoachResponse.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Coach endpoint not yet implemented.",
    )
