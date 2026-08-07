"""
api/upload.py — CSV file upload endpoint.

Accepts a multipart/form-data CSV file, persists it, and triggers
the data-processing pipeline asynchronously.

TODO: Implement file validation (MIME type, size limits).
TODO: Trigger processing pipeline via orchestration layer.
TODO: Return session ID for subsequent API calls.
"""

from __future__ import annotations

from fastapi import APIRouter, File, UploadFile, HTTPException, status
from app.schemas.upload import UploadResponse

router = APIRouter()


@router.post(
    "/",
    response_model=UploadResponse,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Upload a bank transaction CSV",
    description=(
        "Accept a CSV file containing bank transactions. "
        "Returns a session_id used by all subsequent endpoints."
    ),
)
async def upload_csv(file: UploadFile = File(...)) -> UploadResponse:
    """
    Handle CSV upload.

    TODO: Validate file extension and MIME type.
    TODO: Save file to temporary storage.
    TODO: Enqueue processing job via orchestration layer.
    TODO: Return session_id pointing to the processing job.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Upload endpoint not yet implemented.",
    )
