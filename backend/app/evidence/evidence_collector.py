"""
evidence/evidence_collector.py — Persists bias detection results to DB.

Takes a list of DetectionResults from the DetectorRegistry and writes
DetectedBehaviour and BehaviourEvidence records to the database.
"""

from __future__ import annotations

from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from loguru import logger

from app.behaviours.base_detector import DetectionResult
from app.models.behaviour import DetectedBehaviour
from app.models.evidence import BehaviourEvidence


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
        """
        try:
            # Handle duplicate detection runs: deduplicate by removing existing results
            existing_behaviours = (
                self._db.query(DetectedBehaviour)
                .filter(DetectedBehaviour.session_id == session_id)
                .all()
            )
            
            for b in existing_behaviours:
                self._db.query(BehaviourEvidence).filter(
                    BehaviourEvidence.behaviour_id == b.id
                ).delete(synchronize_session=False)
                
            self._db.query(DetectedBehaviour).filter(
                DetectedBehaviour.session_id == session_id
            ).delete(synchronize_session=False)
            
            self._db.flush()

            # Iterate through results and save detected behaviours and evidence
            for result in results:
                if not result.detected:
                    continue

                # Create DetectedBehaviour DB record
                behaviour = DetectedBehaviour(
                    session_id=session_id,
                    bias_type=result.bias_type.value,
                    confidence=result.confidence,
                    severity=result.severity.value,
                    summary=result.summary,
                )
                self._db.add(behaviour)
                self._db.flush()  # Get generated primary key (id)

                # Create BehaviourEvidence records for each evidence_id
                for tx_id in result.evidence_ids:
                    evidence = BehaviourEvidence(
                        behaviour_id=behaviour.id,
                        transaction_id=tx_id,
                        explanation=f"Transaction {tx_id} provides evidence for {result.bias_type.value}",
                        weight=1.0,
                    )
                    self._db.add(evidence)

            self._db.commit()
            logger.info(
                f"Successfully persisted evidence for session {session_id} "
                f"({len([r for r in results if r.detected])} behaviours detected)."
            )

        except SQLAlchemyError as e:
            self._db.rollback()
            logger.error(
                f"Database error while persisting evidence for session {session_id}: {e}", 
                exc_info=True
            )
            raise
        except Exception as e:
            self._db.rollback()
            logger.error(
                f"Unexpected error while persisting evidence for session {session_id}: {e}", 
                exc_info=True
            )
            raise
