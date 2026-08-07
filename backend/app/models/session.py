"""
models/session.py — UploadSession ORM model.

Tracks the lifecycle of a CSV upload from ingestion through
processing, analysis, and completion.

TODO: Add foreign key relationships to Transaction, DetectedBehaviour, ActionPlanItem.
TODO: Add indexes on status and created_at for efficient querying.
"""

from __future__ import annotations

import uuid
from datetime import datetime
from sqlalchemy import String, DateTime, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column
from app.config.database import Base

# TODO: Replace with a proper enum when status values are finalised.
# Possible values: pending | processing | completed | failed
SESSION_STATUS_VALUES = ("pending", "processing", "completed", "failed")


class UploadSession(Base):
    """
    Represents a single CSV upload and its processing lifecycle.

    Attributes:
        id          Unique session identifier (UUID).
        filename    Original CSV filename.
        status      Current processing status.
        created_at  Timestamp of creation.
        updated_at  Timestamp of last update.
        error_msg   Optional error message if processing failed.
    """

    __tablename__ = "upload_sessions"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        comment="UUID session identifier.",
    )
    filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="Original uploaded filename.",
    )
    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="pending",
        comment="Processing lifecycle status.",
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
    error_msg: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
        comment="Error message if processing failed.",
    )

    def __repr__(self) -> str:
        return f"<UploadSession id={self.id!r} status={self.status!r}>"
