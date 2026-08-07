"""
evidence/evidence_formatter.py — Formats DB evidence records into API schemas.

Converts ORM records from DetectedBehaviour + BehaviourEvidence
tables into Pydantic API response schemas.

TODO: Implement ORM → schema mapping.
TODO: Enrich evidence with transaction details (date, amount, description).
"""

from __future__ import annotations

from typing import List
from sqlalchemy.orm import Session

from app.schemas.behaviours import BehaviourDetail


class EvidenceFormatter:
    """Formats database evidence records into API response schemas."""

    def __init__(self, db: Session) -> None:
        self._db = db

    async def format_behaviours(self, session_id: str) -> List[BehaviourDetail]:
        """
        Load and format all behaviour + evidence records for a session.

        TODO: Query DetectedBehaviour for session_id.
        TODO: For each behaviour, load BehaviourEvidence records.
        TODO: Join Transaction records for evidence descriptions.
        TODO: Map to BehaviourDetail Pydantic schema.
        """
        raise NotImplementedError("EvidenceFormatter.format_behaviours not implemented.")
