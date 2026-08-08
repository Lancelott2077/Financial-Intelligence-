"""
decisions/rules.py — Individual rule definitions.

Each rule specifies a trigger condition (bias type + threshold),
a recommendation template, and a priority score.

TODO: Implement all rule definitions.
TODO: Load rule parameters from configuration file.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List

from app.behaviours.base_detector import DetectionResult


@dataclass
class Rule:
    """
    A single decision rule.

    Attributes:
        rule_id         Unique rule identifier.
        trigger_bias    Bias type that activates this rule.
        min_confidence  Minimum detector confidence to trigger.
        title           Recommendation title template.
        description     Recommendation description template.
        priority        'high' | 'medium' | 'low'.
        saving_formula  Function that computes estimated monthly saving.
    """

    rule_id: str
    trigger_bias: str
    min_confidence: float
    title: str
    description: str
    priority: str = "medium"
    saving_formula: Callable[[dict], float] | None = None


RULES: List[Rule] = [
    Rule(
        rule_id="R001",
        trigger_bias="present_bias",
        min_confidence=0.5,
        title="Introduce a 48-Hour Cooling Period",
        description=(
            "Your data shows impulse spending near payday and on weekends. "
            "Before any non-essential purchase over ₹500, wait 48 hours. "
            "This single habit reduces unplanned spending by 15–25% on average."
        ),
        priority="high",
        saving_formula=lambda s: s.get("avg_weekend_spend", 0) * 0.20,
    ),
    Rule(
        rule_id="R002",
        trigger_bias="mental_accounting",
        min_confidence=0.5,
        title="Set a Monthly Discretionary Budget",
        description=(
            "You treat money in different categories as unrelated pools, leading to "
            "overspending in entertainment and dining while under-spending on savings. "
            "Set a single monthly discretionary cap of ₹3,000 across all non-essential categories."
        ),
        priority="medium",
        saving_formula=lambda s: s.get("entertainment_spend", 0) * 0.15,
    ),
    Rule(
        rule_id="R003",
        trigger_bias="loss_aversion",
        min_confidence=0.5,
        title="Automate Emergency Fund Transfers",
        description=(
            "Fear of losing money prevents you from moving funds to higher-yield accounts. "
            "Set up an automatic transfer of ₹1,000 on payday to a separate emergency fund. "
            "Automation removes the emotional friction that loss aversion creates."
        ),
        priority="high",
        saving_formula=lambda s: 1000.0,
    ),
    Rule(
        rule_id="R004",
        trigger_bias="anchoring",
        min_confidence=0.5,
        title="Reassess Recurring Subscriptions",
        description=(
            "You anchor to original prices and rarely reassess subscriptions. "
            "Review all recurring charges monthly and cancel any service unused in the last 30 days. "
            "Users typically save ₹500–₹2,000 per month from this single action."
        ),
        priority="medium",
        saving_formula=lambda s: s.get("subscription_spend", 0) * 0.30,
    ),
    Rule(
        rule_id="R005",
        trigger_bias="status_quo_bias",
        min_confidence=0.5,
        title="Switch to a Higher-Yield Savings Account",
        description=(
            "Inertia is keeping your savings in a low-interest account. "
            "Moving your balance to a high-yield account takes under 30 minutes "
            "and adds 4–6% annual interest with zero additional effort."
        ),
        priority="low",
        saving_formula=lambda s: s.get("avg_balance", 0) * 0.05 / 12,
    ),
]
