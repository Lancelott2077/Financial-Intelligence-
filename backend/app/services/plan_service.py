"""
services/plan_service.py — Action Plan generation and management service.

Generates a prioritised, time-bound action plan from detected behaviours
and savings opportunities.

TODO: Implement plan item generation logic.
TODO: Implement plan item status update (complete / skip).
TODO: Re-generate plan after new behaviours are detected.
"""

from __future__ import annotations

from sqlalchemy.orm import Session
from app.schemas.plan import PlanResponse


class PlanService:
    """Service for generating and managing personalised action plans."""

    def __init__(self, db: Session) -> None:
        self._db = db

    async def generate_plan(self, session_id: str) -> PlanResponse:
        """
        Generate or retrieve the action plan for a session.

        TODO: Load behaviours and savings opportunities for the session.
        TODO: Convert each high/medium severity behaviour into a plan item.
        TODO: Assign priority, estimated saving, and target date.
        TODO: Persist plan items and return PlanResponse.
        """
        raise NotImplementedError("PlanService.generate_plan not implemented.")

    async def update_item_status(
        self, session_id: str, item_id: int, status: str
    ) -> None:
        """
        Update the status of a plan item.

        TODO: Validate status value (pending | in_progress | completed | skipped).
        TODO: Update ActionPlanItem.status in the database.
        """
        raise NotImplementedError("PlanService.update_item_status not implemented.")
