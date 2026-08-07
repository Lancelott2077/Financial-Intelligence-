"""
decisions/decision_builder.py — Assembles recommendations into an action plan.

Converts the output of RuleEngine.evaluate() into ActionPlanItem
database records ready for persistence.

TODO: Implement plan item construction.
TODO: Assign target_date based on priority.
"""

from __future__ import annotations

from typing import List
from sqlalchemy.orm import Session

from app.decisions.rule_engine import Recommendation
from app.models.plan import ActionPlanItem


class DecisionBuilder:
    """Converts rule engine recommendations into ActionPlanItem records."""

    def __init__(self, db: Session) -> None:
        self._db = db

    async def build_plan(
        self, session_id: str, recommendations: List[Recommendation]
    ) -> List[ActionPlanItem]:
        """
        Create and persist ActionPlanItem records for each recommendation.

        Args:
            session_id:         UUID of the UploadSession.
            recommendations:    List of Recommendations from RuleEngine.

        Returns:
            List of persisted ActionPlanItem ORM objects.

        TODO: Map Recommendation fields to ActionPlanItem columns.
        TODO: Calculate target_date (high=30 days, medium=60 days, low=90 days).
        TODO: Persist and commit to DB.
        """
        raise NotImplementedError("DecisionBuilder.build_plan not implemented.")
