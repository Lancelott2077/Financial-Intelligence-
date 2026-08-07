"""
models/evidence.py — BehaviourEvidence ORM model.

Stores the transaction-level evidence that supports a detected behaviour.
Links a DetectedBehaviour to one or more Transactions with an explanation.

TODO: Add ForeignKey to DetectedBehaviour.id and Transaction.id.
"""

from __future__ import annotations

from sqlalchemy import String, Integer, Text, Float
from sqlalchemy.orm import Mapped, mapped_column
from app.config.database import Base


class BehaviourEvidence(Base):
    """
    Evidence record linking a behaviour to a specific transaction.

    Attributes:
        id                  Surrogate primary key.
        behaviour_id        Reference to DetectedBehaviour.
        transaction_id      Reference to Transaction.
        explanation         Why this transaction is evidence of the bias.
        weight              Contribution weight to the overall confidence score.
    """

    __tablename__ = "behaviour_evidence"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    behaviour_id: Mapped[int] = mapped_column(
        Integer, nullable=False, index=True, comment="Parent DetectedBehaviour."
    )
    transaction_id: Mapped[int] = mapped_column(
        Integer, nullable=False, index=True, comment="Supporting Transaction."
    )
    explanation: Mapped[str | None] = mapped_column(
        Text, nullable=True, comment="Human-readable evidence explanation."
    )
    weight: Mapped[float] = mapped_column(
        Float, nullable=False, default=1.0, comment="Evidence weight 0.0–1.0."
    )

    def __repr__(self) -> str:
        return (
            f"<BehaviourEvidence behaviour={self.behaviour_id} "
            f"transaction={self.transaction_id}>"
        )
