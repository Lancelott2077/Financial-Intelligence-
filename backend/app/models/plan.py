"""
models/plan.py — ActionPlanItem ORM model.

Stores a single actionable recommendation in the personalised
financial action plan.

TODO: Add ForeignKey to UploadSession.id and DetectedBehaviour.id.
TODO: Add status enum: pending | in_progress | completed | skipped.
"""

from __future__ import annotations

from datetime import date, datetime
from sqlalchemy import String, Date, DateTime, Text, Float
from sqlalchemy.orm import Mapped, mapped_column
from app.config.database import Base


class ActionPlanItem(Base):
    """
    A single item in the user's personalised financial action plan.

    Attributes:
        id                  Surrogate primary key.
        session_id          Reference to UploadSession.
        behaviour_id        Optional reference to the triggering behaviour.
        title               Short title of the action item.
        description         Detailed description and rationale.
        estimated_saving    Projected monthly saving (currency units).
        priority            Priority: high | medium | low.
        target_date         Target completion date.
        status              Current status: pending | in_progress | completed | skipped.
        created_at          Timestamp of creation.
    """

    __tablename__ = "action_plan_items"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    session_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    behaviour_id: Mapped[int | None] = mapped_column(
        nullable=True, comment="Optional triggering behaviour."
    )
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    estimated_saving: Mapped[float] = mapped_column(
        Float, nullable=False, default=0.0
    )
    priority: Mapped[str] = mapped_column(
        String(20), nullable=False, default="medium", comment="high | medium | low."
    )
    target_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    status: Mapped[str] = mapped_column(
        String(20), nullable=False, default="pending"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.utcnow
    )

    def __repr__(self) -> str:
        return f"<ActionPlanItem id={self.id} title={self.title!r} status={self.status!r}>"
