"""
models/behaviour.py — DetectedBehaviour ORM model.

Stores a behavioural bias identified by the behaviour detection engine
for a given session.

TODO: Add ForeignKey to UploadSession.id.
TODO: Add relationship to BehaviourEvidence.
TODO: Define full list of bias_type values via an enum.
"""

from __future__ import annotations

from datetime import datetime
from sqlalchemy import String, DateTime, Float, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.config.database import Base


class DetectedBehaviour(Base):
    """
    A cognitive / behavioural bias detected in a user's spending patterns.

    Attributes:
        id              Surrogate primary key.
        session_id      Reference to the parent UploadSession.
        bias_type       Type of bias (e.g., "present_bias", "loss_aversion").
        confidence      Confidence score 0.0–1.0.
        severity        Severity level: low | medium | high.
        summary         Human-readable description of the detected bias.
        detected_at     Timestamp of detection.
    """

    __tablename__ = "detected_behaviours"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    session_id: Mapped[str] = mapped_column(
        String(36), nullable=False, index=True
    )
    bias_type: Mapped[str] = mapped_column(
        String(100), nullable=False, comment="Bias type identifier."
    )
    confidence: Mapped[float] = mapped_column(
        Float, nullable=False, default=0.0, comment="Confidence score 0.0–1.0."
    )
    severity: Mapped[str] = mapped_column(
        String(20), nullable=False, default="low", comment="low | medium | high."
    )
    summary: Mapped[str | None] = mapped_column(
        Text, nullable=True, comment="Human-readable summary."
    )
    detected_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.utcnow
    )

    def __repr__(self) -> str:
        return (
            f"<DetectedBehaviour id={self.id} bias={self.bias_type!r} "
            f"confidence={self.confidence:.2f}>"
        )
