"""
decisions/decision_builder.py — Assembles recommendations into an action plan.

Converts the output of RuleEngine.evaluate() into ActionPlanItem
database records ready for persistence.
"""

from __future__ import annotations

from datetime import date, timedelta
from typing import List
from sqlalchemy.orm import Session

from app.decisions.rule_engine import Recommendation
from app.models.plan import ActionPlanItem


_PRIORITY_DAYS = {"high": 30, "medium": 60, "low": 90}


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
        """
        # Clear any previous plan items for this session (idempotent)
        self._db.query(ActionPlanItem).filter(
            ActionPlanItem.session_id == session_id
        ).delete(synchronize_session=False)

        items: List[ActionPlanItem] = []
        today = date.today()

        for rec in recommendations:
            days = _PRIORITY_DAYS.get(rec.priority, 60)
            target = today + timedelta(days=days)

            item = ActionPlanItem(
                session_id=session_id,
                title=rec.title,
                description=rec.description,
                estimated_saving=rec.estimated_saving,
                priority=rec.priority,
                target_date=target,
                status="pending",
            )
            self._db.add(item)
            items.append(item)

        self._db.commit()
        for item in items:
            self._db.refresh(item)

        return items

