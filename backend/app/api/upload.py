"""
api/upload.py — CSV file upload endpoint.

Accepts a multipart/form-data CSV file, persists it, and triggers
the data-processing pipeline asynchronously.
"""

from __future__ import annotations

from fastapi import APIRouter, File, UploadFile, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.schemas.upload import UploadResponse
from app.config.database import get_db
from app.services.upload_service import UploadService

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
async def upload_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
) -> UploadResponse:
    """
    Handle CSV upload.
    """
    # Validate file extension and MIME type
    is_valid_ext = file.filename and file.filename.lower().endswith(".csv")
    is_valid_mime = file.content_type == "text/csv"
    
    if not is_valid_ext or not is_valid_mime:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type. Only CSV files are supported.",
        )
            
    # Read raw bytes
    try:
        file_content = await file.read()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Could not read uploaded file: {e}",
        )
        
    # Delegate to orchestration service
    service = UploadService(db)
    try:
        session_id = await service.create_session(file.filename, file_content)
    except RuntimeError as e:
        # UploadService internally updates the DB to FAILED on error.
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Processing failed: {e}",
        )
        
    return UploadResponse(session_id=session_id)
