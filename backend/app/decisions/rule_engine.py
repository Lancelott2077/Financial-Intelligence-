"""
decisions/rule_engine.py — Core rule evaluation engine.

Evaluates a set of financial rules against detected behaviours
and snapshot data to produce a prioritised list of recommendations.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from app.behaviours.base_detector import DetectionResult
from app.decisions.rules import RULES


_PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


@dataclass
class Recommendation:
    """
    A single recommendation produced by the rule engine.

    Attributes:
        rule_id             Unique identifier of the triggering rule.
        title               Short recommendation title.
        description         Detailed rationale and action steps.
        priority            'high' | 'medium' | 'low'.
        estimated_saving    Projected monthly saving.
        linked_behaviour    Bias type that triggered this recommendation.
    """

    rule_id: str
    title: str
    description: str
    priority: str = "medium"
    estimated_saving: float = 0.0
    linked_behaviour: str | None = None


class RuleEngine:
    """Evaluates registered rules against detection results."""

    def evaluate(
        self,
        detection_results: List[DetectionResult],
        snapshot_data: dict,
    ) -> List[Recommendation]:
        """
        Evaluate all rules and return ranked recommendations.

        Args:
            detection_results:  Results from DetectorRegistry.run_all().
            snapshot_data:      Aggregated financial snapshot dict (may be empty).

        Returns:
            List of Recommendation, sorted by priority then estimated saving.
        """
        # Build a quick-lookup dict: bias_type_string → DetectionResult
        detected_map = {
            r.bias_type.value: r
            for r in detection_results
            if r.detected
        }

        recommendations: List[Recommendation] = []

        for rule in RULES:
            result = detected_map.get(rule.trigger_bias)
            if result is None:
                continue
            if result.confidence < rule.min_confidence:
                continue

            saving = 0.0
            if rule.saving_formula is not None:
                try:
                    saving = float(rule.saving_formula(snapshot_data))
                except Exception:
                    saving = 0.0

            recommendations.append(
                Recommendation(
                    rule_id=rule.rule_id,
                    title=rule.title,
                    description=rule.description,
                    priority=rule.priority,
                    estimated_saving=round(saving, 2),
                    linked_behaviour=rule.trigger_bias,
                )
            )

        # Sort by priority (high→low) then estimated_saving (desc)
        recommendations.sort(
            key=lambda r: (_PRIORITY_ORDER.get(r.priority, 1), -r.estimated_saving)
        )

        return recommendations

