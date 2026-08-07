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


# TODO: Define all rules below following the Rule dataclass structure.
# Example structure (not implemented):
# RULES: List[Rule] = [
#     Rule(
#         rule_id="R001",
#         trigger_bias="present_bias",
#         min_confidence=0.6,
#         title="Reduce impulse spending after payday",
#         description="...",
#         priority="high",
#         saving_formula=lambda snapshot: snapshot.get("dining_spend", 0) * 0.2,
#     ),
# ]

RULES: List[Rule] = []  # TODO: Populate with rule definitions.
