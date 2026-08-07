"""schemas/upload.py — Upload endpoint Pydantic schemas."""

from __future__ import annotations

from app.schemas.common import BaseResponse, ProcessingStatus


class UploadResponse(BaseResponse):
    """
    Response returned after a successful CSV upload.

    Attributes:
        session_id  UUID identifying this upload session.
        status      Initial processing status (always 'pending').
        message     Human-readable status message.
    """

    session_id: str
    status: ProcessingStatus = ProcessingStatus.PENDING
    message: str = "File uploaded successfully. Processing will begin shortly."
