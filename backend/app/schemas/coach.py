"""schemas/coach.py — AI Financial Coach Pydantic schemas."""

from __future__ import annotations

from typing import List
from pydantic import Field
from app.schemas.common import BaseResponse


class ChatMessage(BaseResponse):
    """A single message in the coaching conversation history."""

    role: str = Field(description="'user' or 'assistant'.")
    content: str


class CoachRequest(BaseResponse):
    """Request body for a coaching conversation turn."""

    session_id: str
    message: str = Field(min_length=1, max_length=2000)
    history: List[ChatMessage] = Field(default_factory=list)


class CoachResponse(BaseResponse):
    """
    AI coach response for a single conversation turn.

    TODO: Populate from CoachService via GeminiClient.
    """

    session_id: str
    reply: str = ""
    references: List[str] = Field(
        default_factory=list,
        description="Referenced behaviour IDs or plan items.",
    )
