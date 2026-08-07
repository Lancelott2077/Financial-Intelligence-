"""
services/upload_service.py — Upload session management service.

Responsible for:
    - Persisting the uploaded CSV file to disk / storage.
    - Creating an UploadSession database record.
    - Triggering the downstream processing pipeline.
"""

from __future__ import annotations

import logging
from pathlib import Path
from sqlalchemy.orm import Session

from app.models.session import UploadSession
from app.schemas.common import ProcessingStatus
from app.processing.pipeline import ProcessingPipeline

logger = logging.getLogger(__name__)


class UploadService:
    """Service for managing CSV upload sessions."""

    def __init__(self, db: Session) -> None:
        self._db = db

    async def create_session(self, filename: str, file_content: bytes) -> str:
        """
        Persist the uploaded file, create an UploadSession, and execute the processing pipeline.

        Args:
            filename:       Original filename of the uploaded CSV.
            file_content:   Raw bytes of the uploaded file.

        Returns:
            The UUID session_id of the newly created session.
        """
        # 1. Sanitize filename to prevent path traversal and create UploadSession
        safe_filename = Path(filename).name
        
        session_record = UploadSession(
            filename=safe_filename,
            status=ProcessingStatus.PENDING.value
        )
        self._db.add(session_record)
        self._db.commit()
        self._db.refresh(session_record)
        
        session_id = session_record.id
        logger.info("Created UploadSession %s for file %s", session_id, safe_filename)
        
        # 2. Save file to local storage
        upload_dir = Path("uploads")
        upload_dir.mkdir(parents=True, exist_ok=True)
        file_path = upload_dir / f"{session_id}_{safe_filename}"
        
        try:
            with open(file_path, "wb") as f:
                f.write(file_content)
            logger.debug("File saved to %s", file_path)
        except OSError as e:
            logger.error("Failed to save file for session %s: %s", session_id, e)
            session_record.status = ProcessingStatus.FAILED.value
            session_record.error_msg = f"Storage error: {e}"[:1000]
            self._db.commit()
            raise RuntimeError(f"Storage error for session {session_id}") from e

        # 3. Update status and trigger pipeline
        session_record.status = ProcessingStatus.PROCESSING.value
        self._db.commit()
        
        try:
            pipeline = ProcessingPipeline(self._db)
            await pipeline.run(session_id, file_path)
            
            # 4. Mark as completed on success
            session_record.status = ProcessingStatus.COMPLETED.value
            self._db.commit()
            logger.info("UploadSession %s completed successfully", session_id)
            
        except RuntimeError as e:
            # 5. Handle pipeline failure gracefully by updating session state
            session_record.status = ProcessingStatus.FAILED.value
            session_record.error_msg = str(e)[:1000]
            self._db.commit()
            logger.error("UploadSession %s failed: %s", session_id, e)
            # Re-raise to ensure the caller/API layer is aware of the failure
            raise
            
        return session_id

    async def get_session_status(self, session_id: str) -> dict:
        """
        Return the current status of an upload session.
        
        Args:
            session_id: The UUID of the session to query.
            
        Returns:
            Dictionary containing id, status, created_at, updated_at, and error_msg.
            
        Raises:
            ValueError: If the session does not exist.
        """
        session_record = self._db.query(UploadSession).filter(UploadSession.id == session_id).first()
        if not session_record:
            logger.warning("Session status requested for unknown session_id: %s", session_id)
            raise ValueError(f"UploadSession {session_id} not found")
            
        return {
            "id": session_record.id,
            "status": session_record.status,
            "created_at": session_record.created_at.isoformat(),
            "updated_at": session_record.updated_at.isoformat(),
            "error_msg": session_record.error_msg
        }
