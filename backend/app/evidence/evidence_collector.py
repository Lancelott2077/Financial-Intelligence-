"""
evidence/evidence_collector.py — Persists bias detection results to DB.

Takes a list of DetectionResults from the DetectorRegistry and writes
DetectedBehaviour and BehaviourEvidence records to the database.

TODO: Implement full persistence logic.
TODO: Handle duplicate detection runs (upsert or deduplicate).
"""

from __future__ import annotations

from typing import List
from sqlalchemy.orm import Session

from app.behaviours.base_detector import DetectionResult


class EvidenceCollector:
    """Persists DetectionResults to the database."""

    def __init__(self, db: Session) -> None:
        self._db = db

    async def persist(
        self, session_id: str, results: List[DetectionResult]
    ) -> None:
        """
        Persist all detection results for a session.

        Args:
            session_id: UUID of the parent UploadSession.
            results:    List of DetectionResults from DetectorRegistry.

        TODO: For each result where detected=True:
            - Create DetectedBehaviour DB record.
            - Create BehaviourEvidence records for each evidence_id.
        TODO: Commit DB session.
        TODO: Handle DB errors and rollback.
        """
        raise NotImplementedError("EvidenceCollector.persist not implemented.")
