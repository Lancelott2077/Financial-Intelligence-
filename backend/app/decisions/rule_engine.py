"""
decisions/rule_engine.py — Core rule evaluation engine.

Evaluates a set of financial rules against detected behaviours
and snapshot data to produce a prioritised list of recommendations.

TODO: Implement rule evaluation pipeline.
TODO: Support rule weights and priority scoring.
TODO: Support rule enable/disable configuration.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from app.behaviours.base_detector import DetectionResult


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
            snapshot_data:      Aggregated financial snapshot dict.

        Returns:
            List of Recommendation, sorted by priority and estimated saving.

        TODO: Load rule definitions from rules.py.
        TODO: For each rule, check trigger condition against detections.
        TODO: Compute estimated_saving for triggered rules.
        TODO: Sort by priority score descending.
        """
        raise NotImplementedError("RuleEngine.evaluate not implemented.")
