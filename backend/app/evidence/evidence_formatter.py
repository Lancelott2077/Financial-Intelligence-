"""
evidence/evidence_formatter.py — Formats DB evidence records into API schemas.

Converts ORM records from DetectedBehaviour + BehaviourEvidence
tables into Pydantic API response schemas.
"""

from __future__ import annotations

from typing import List
from sqlalchemy.orm import Session

from app.schemas.behaviours import BehaviourDetail, EvidenceItem
from app.schemas.common import BiasType, SeverityLevel, SpendingCategory
from app.models.behaviour import DetectedBehaviour
from app.models.evidence import BehaviourEvidence
from app.models.transaction import Transaction


class EvidenceFormatter:
    """Formats database evidence records into API response schemas."""

    def __init__(self, db: Session) -> None:
        self._db = db

    async def format_behaviours(self, session_id: str) -> List[BehaviourDetail]:
        """
        Load and format all behaviour + evidence records for a session.
        """
        # Query DetectedBehaviour for session_id.
        behaviours = (
            self._db.query(DetectedBehaviour)
            .filter(DetectedBehaviour.session_id == session_id)
            .all()
        )
        
        formatted_behaviours: List[BehaviourDetail] = []
        
        for b in behaviours:
            # For each behaviour, load BehaviourEvidence records and
            # join Transaction records for evidence descriptions.
            evidence_records = (
                self._db.query(BehaviourEvidence, Transaction)
                .join(Transaction, BehaviourEvidence.transaction_id == Transaction.id)
                .filter(BehaviourEvidence.behaviour_id == b.id)
                .all()
            )
            
            evidence_items: List[EvidenceItem] = []
            for ev, tx in evidence_records:
                evidence_items.append(
                    EvidenceItem(
                        transaction_id=tx.id,
                        date=tx.date.isoformat(),
                        description=tx.description,
                        amount=float(tx.amount),
                        category=tx.category or SpendingCategory.OTHER.value,
                        explanation=ev.explanation or ""
                    )
                )
                
            display_name = str(b.bias_type).replace("_", " ").title()
                
            # Map to BehaviourDetail Pydantic schema.
            detail = BehaviourDetail(
                id=b.id,
                bias_type=BiasType(b.bias_type),
                display_name=display_name,
                confidence=b.confidence,
                severity=SeverityLevel(b.severity),
                detected=True,
                summary=b.summary or "",
                evidence=evidence_items
            )
            formatted_behaviours.append(detail)
            
        return formatted_behaviours
