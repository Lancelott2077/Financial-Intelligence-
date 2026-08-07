"""schemas/common.py — Shared base models, enums, and utilities."""

from __future__ import annotations

from enum import Enum
from pydantic import BaseModel, ConfigDict


class BaseResponse(BaseModel):
    """Common response wrapper."""

    model_config = ConfigDict(from_attributes=True)


class SeverityLevel(str, Enum):
    """Severity level for detected behaviours and plan items."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class ProcessingStatus(str, Enum):
    """Upload session processing lifecycle status."""

    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
