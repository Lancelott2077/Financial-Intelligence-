"""
models/transaction.py — Transaction ORM model.

Represents a single normalised bank transaction row after CSV ingestion
and preprocessing.

TODO: Add ForeignKey to UploadSession.id.
TODO: Add index on session_id, date, and category.
TODO: Add column for embedding vector once AI enrichment is added.
"""

from __future__ import annotations

from datetime import date
from decimal import Decimal
from sqlalchemy import String, Date, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.config.database import Base


class Transaction(Base):
    """
    A single normalised bank transaction.

    Attributes:
        id              Surrogate primary key.
        session_id      Reference to the parent UploadSession.
        date            Transaction date.
        description     Raw transaction description / narration.
        amount          Transaction amount (positive = credit, negative = debit).
        category        AI / rule-assigned spending category.
        merchant        Extracted merchant name.
        currency        ISO 4217 currency code (default: INR).
    """

    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    session_id: Mapped[str] = mapped_column(
        String(36),
        # TODO: ForeignKey("upload_sessions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="Parent upload session.",
    )
    date: Mapped[date] = mapped_column(Date, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    category: Mapped[str | None] = mapped_column(
        String(100), nullable=True, comment="Spending category."
    )
    merchant: Mapped[str | None] = mapped_column(
        String(200), nullable=True, comment="Extracted merchant name."
    )
    currency: Mapped[str] = mapped_column(String(3), nullable=False, default="INR")

    def __repr__(self) -> str:
        return (
            f"<Transaction id={self.id} date={self.date} "
            f"amount={self.amount} category={self.category!r}>"
        )
