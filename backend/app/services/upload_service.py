"""
services/upload_service.py — Upload session management service.

Responsible for:
    - Persisting the uploaded CSV file to disk / storage.
    - Creating an UploadSession database record.
    - Triggering the downstream processing pipeline.

TODO: Implement file storage (local disk initially, S3 later).
TODO: Implement session creation in database.
TODO: Trigger orchestration pipeline with session_id.
"""

from __future__ import annotations

from sqlalchemy.orm import Session


class UploadService:
    """Service for managing CSV upload sessions."""

    def __init__(self, db: Session) -> None:
        self._db = db

    async def create_session(self, filename: str, file_content: bytes) -> str:
        """
        Persist the uploaded file and create a new UploadSession record.

        Args:
            filename:       Original filename of the uploaded CSV.
            file_content:   Raw bytes of the uploaded file.

        Returns:
            The UUID session_id of the newly created session.

        TODO: Save file_content to configured storage path.
        TODO: Insert UploadSession row with status='pending'.
        TODO: Return the new session_id.
        """
        raise NotImplementedError("UploadService.create_session not implemented.")

    async def get_session_status(self, session_id: str) -> dict:
        """
        Return the current status of an upload session.

        TODO: Query UploadSession by session_id.
        TODO: Return status dict with id, status, created_at, updated_at.
        """
        raise NotImplementedError("UploadService.get_session_status not implemented.")
