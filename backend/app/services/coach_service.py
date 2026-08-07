"""
services/coach_service.py — AI Financial Coach conversation service.

Manages multi-turn coaching conversations backed by Gemini.
Grounds responses in the user's actual financial data.

TODO: Implement conversation context loading.
TODO: Implement Gemini prompt construction.
TODO: Implement conversation history persistence.
"""

from __future__ import annotations

from sqlalchemy.orm import Session
from app.schemas.coach import CoachRequest, CoachResponse


class CoachService:
    """Service for managing AI coaching conversations."""

    def __init__(self, db: Session) -> None:
        self._db = db

    async def chat(self, request: CoachRequest) -> CoachResponse:
        """
        Process a user message and return a coaching response.

        TODO: Load session financial context (snapshot, behaviours, plan).
        TODO: Build system prompt with context from prompts/ directory.
        TODO: Append conversation history to the prompt.
        TODO: Call GeminiClient.generate(prompt).
        TODO: Parse response and extract referenced behaviour/plan IDs.
        TODO: Persist conversation turn in database.
        """
        raise NotImplementedError("CoachService.chat not implemented.")
