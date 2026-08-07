"""schemas/behaviours.py — Detected Behaviours Pydantic schemas."""

from __future__ import annotations

from typing import List
from pydantic import Field
from app.schemas.common import BaseResponse, SeverityLevel


class EvidenceItem(BaseResponse):
    """A single piece of evidence supporting a detected behaviour."""

    transaction_id: int
    date: str
    description: str
    amount: float
    explanation: str


class BehaviourDetail(BaseResponse):
    """Detail of a single detected behavioural bias."""

    id: int
    bias_type: str = Field(description="Bias identifier, e.g. 'present_bias'.")
    display_name: str = Field(description="Human-readable bias name.")
    confidence: float = Field(ge=0.0, le=1.0)
    severity: SeverityLevel
    summary: str
    evidence: List[EvidenceItem] = Field(default_factory=list)


class BehavioursResponse(BaseResponse):
    """
    List of all detected behavioural biases for an upload session.

    TODO: Populate from BehaviourService.get_behaviours().
    """

    session_id: str
    behaviours: List[BehaviourDetail] = Field(default_factory=list)
    total_count: int = 0
