"""
schemas/common.py — Shared base models, enums, and utilities.

This module is the SINGLE SOURCE OF TRUTH for all enumerated types.
Every other schema module imports enums from here — never define
duplicate enum values in other modules.

Enum ownership:
    SeverityLevel       Used by: BehaviourDetail, SavingOpportunity, PlanItem
    ProcessingStatus    Used by: UploadResponse
    BiasType            Used by: BehaviourDetail, DetectionResult, BehaviourProfile
    PlanItemStatus      Used by: PlanItem
    MessageRole         Used by: ChatMessage
    TransactionType     Used by: Transaction processing layer
    DifficultyLevel     Alias of SeverityLevel for readability in savings context
"""

from __future__ import annotations

from enum import Enum
from pydantic import BaseModel, ConfigDict


class BaseResponse(BaseModel):
    """
    Common base for all API response and request models.

    Enables ORM-mode so SQLAlchemy models can be passed directly
    to response_model serialisation.
    """

    model_config = ConfigDict(from_attributes=True)


# ── Severity / Priority ───────────────────────────────────────────────────────

class SeverityLevel(str, Enum):
    """
    Tri-level severity / priority scale.

    Used by:  BehaviourDetail.severity, SavingOpportunity.difficulty, PlanItem.priority
    Values:   low | medium | high
    """

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


# DifficultyLevel is an alias so savings-context code reads naturally.
DifficultyLevel = SeverityLevel


# ── Upload Session ────────────────────────────────────────────────────────────

class ProcessingStatus(str, Enum):
    """
    Upload session lifecycle status.

    Used by:  UploadResponse.status
    Flow:     pending → processing → completed | failed
    """

    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


# ── Bias Detection ────────────────────────────────────────────────────────────

class BiasType(str, Enum):
    """
    Registry of all supported cognitive / behavioural bias identifiers.

    Used by:  BehaviourDetail.bias_type, DetectionResult.bias_type,
              BehaviourProfile, PlanItem.linked_bias_type

    Adding a new bias requires:
        1. Add the value here.
        2. Add a detector in app/behaviours/.
        3. Add a display entry in frontend/types/behaviours.ts BIAS_DISPLAY_META.
        4. Add rules in app/decisions/rules.py.
    """

    PRESENT_BIAS = "present_bias"
    LOSS_AVERSION = "loss_aversion"
    ANCHORING = "anchoring"
    MENTAL_ACCOUNTING = "mental_accounting"
    STATUS_QUO_BIAS = "status_quo_bias"


# ── Action Plan ───────────────────────────────────────────────────────────────

class PlanItemStatus(str, Enum):
    """
    Lifecycle status of a single action plan item.

    Used by:  PlanItem.status
    Flow:     pending → in_progress → completed | skipped
    """

    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    SKIPPED = "skipped"


# ── Coach ─────────────────────────────────────────────────────────────────────

class MessageRole(str, Enum):
    """
    Role of a message in the coaching conversation.

    Used by:  ChatMessage.role
    Values:   user | assistant
    """

    USER = "user"
    ASSISTANT = "assistant"


# ── Transactions ──────────────────────────────────────────────────────────────

class TransactionType(str, Enum):
    """
    Whether a transaction is a debit (money out) or credit (money in).

    Used by:  Transaction processing layer, feature extraction.
    Derived from: sign of the amount column after normalisation.
    """

    DEBIT = "debit"
    CREDIT = "credit"


# ── Spending Categories ───────────────────────────────────────────────────────

class SpendingCategory(str, Enum):
    """
    Taxonomy of spending categories assigned during CSV processing.

    Used by:  Transaction.category, ScenarioChange.category,
              CategoryBreakdown.category, SavingOpportunity.category

    Adding a new category requires updating app/processing/categoriser.py
    and the prompts/categorisation.md template.
    """

    FOOD_AND_DINING = "food_and_dining"
    GROCERIES = "groceries"
    TRANSPORT = "transport"
    ENTERTAINMENT = "entertainment"
    UTILITIES = "utilities"
    HEALTHCARE = "healthcare"
    SHOPPING = "shopping"
    EDUCATION = "education"
    TRAVEL = "travel"
    INCOME = "income"
    TRANSFER = "transfer"
    OTHER = "other"

