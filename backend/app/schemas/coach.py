"""
schemas/coach.py — AI Financial Coach API schemas.

Object ownership:
    ChatMessage     Used by CoachRequest (history) and CoachResponse.
    CoachRequest    Owned by: API layer (app/api/coach.py)
    CoachResponse   Owned by: CoachService via GeminiClient
                    Consumer: Frontend AI Coach page
"""

from __future__ import annotations

from typing import List
from pydantic import Field
from app.schemas.common import BaseResponse, MessageRole


class ChatMessage(BaseResponse):
    """
    A single message in the coaching conversation history.

    Fields:
        role     Who sent the message: 'user' or 'assistant'.
        content  The text content of the message.
    """

    role: MessageRole = Field(description="Message author: 'user' or 'assistant'.")
    content: str = Field(description="Text content of the message.")


class CoachRequest(BaseResponse):
    """
    Request body for a single coaching conversation turn.

    Fields:
        session_id  UUID of the upload session (provides financial context).
        message     The user's current message (1–2000 characters).
        history     All prior turns in the conversation, oldest first.
    """

    session_id: str = Field(description="Upload session UUID for financial context.")
    message: str = Field(
        min_length=1,
        max_length=2000,
        description="The user's current message.",
    )
    history: List[ChatMessage] = Field(
        default_factory=list,
        description="Prior conversation turns, oldest first.",
    )


class CoachResponse(BaseResponse):
    """
    AI coach response for a single conversation turn.

    Fields:
        session_id  UUID of the upload session.
        reply       The AI-generated coaching response text.
        references  Bias type IDs or plan item IDs cited in the reply.
    """

    session_id: str
    reply: str = Field(default="", description="AI-generated coaching response.")
    references: List[str] = Field(
        default_factory=list,
        description="BiasType values or plan item IDs cited in the reply.",
    )
