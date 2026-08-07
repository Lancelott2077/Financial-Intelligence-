"""
services/savings_service.py — Savings opportunities generation service.

Generates ranked savings recommendations by combining behaviour analysis
results and spending patterns.

TODO: Implement opportunity identification from category spend analysis.
TODO: Rank by estimated monthly impact.
TODO: Filter by user-configurable difficulty threshold.
"""

from __future__ import annotations

from sqlalchemy.orm import Session
from app.schemas.savings import SavingsResponse


class SavingsService:
    """Service for generating ranked savings opportunities."""

    def __init__(self, db: Session) -> None:
        self._db = db

    async def get_opportunities(self, session_id: str) -> SavingsResponse:
        """
        Return ranked savings opportunities for the given session.

        TODO: Load snapshot and behaviour data for the session.
        TODO: Identify high-spend categories with reduction potential.
        TODO: Calculate estimated_monthly_saving for each opportunity.
        TODO: Rank and return top N opportunities.
        """
        raise NotImplementedError("SavingsService.get_opportunities not implemented.")
