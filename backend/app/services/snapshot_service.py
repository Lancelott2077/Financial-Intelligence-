"""
services/snapshot_service.py — Financial Snapshot service.

Aggregates raw transaction data into summary statistics for the
Financial Snapshot page.

TODO: Implement income/expense aggregation using pandas.
TODO: Implement category breakdown computation.
TODO: Implement monthly trend time-series computation.
"""

from __future__ import annotations

from sqlalchemy.orm import Session
from app.schemas.snapshot import SnapshotResponse


class SnapshotService:
    """Service for building financial snapshot summaries."""

    def __init__(self, db: Session) -> None:
        self._db = db

    async def build_snapshot(self, session_id: str) -> SnapshotResponse:
        """
        Build and return a financial snapshot for the given session.

        Args:
            session_id: UUID of the upload session.

        Returns:
            Populated SnapshotResponse.

        TODO: Fetch transactions from DB for this session.
        TODO: Compute total_income, total_expenses, net_savings, savings_rate.
        TODO: Compute category_breakdown using pandas groupby.
        TODO: Compute monthly_trends time series.
        """
        raise NotImplementedError("SnapshotService.build_snapshot not implemented.")
