"""
services/behaviour_service.py — Behaviour retrieval and formatting service.

Retrieves detected behaviours from the database and formats them
into API response models.

TODO: Implement behaviour retrieval from DB.
TODO: Join with BehaviourEvidence records.
TODO: Map bias_type codes to display names and descriptions.
"""

from __future__ import annotations

from sqlalchemy.orm import Session
from app.schemas.behaviours import BehavioursResponse


class BehaviourService:
    """Service for retrieving and formatting detected behaviours."""

    def __init__(self, db: Session) -> None:
        self._db = db

    async def get_behaviours(self, session_id: str) -> BehavioursResponse:
        """
        Return all detected behaviours for the given session.

        TODO: Query DetectedBehaviour table filtered by session_id.
        TODO: For each behaviour, load associated BehaviourEvidence records.
        TODO: Map to BehaviourDetail schema including evidence list.
        """
        raise NotImplementedError("BehaviourService.get_behaviours not implemented.")
