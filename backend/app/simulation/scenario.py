"""
simulation/scenario.py — Scenario data models and validation.

Defines the data structures used internally by the simulation engine.

TODO: Add scenario preset templates (e.g., 'reduce dining 20%').
TODO: Add validation for mutually exclusive or conflicting changes.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class ScenarioChange:
    """
    A single behaviour change within a simulation scenario.

    Attributes:
        category        Spending category to modify.
        change_percent  Percentage change (negative = reduction).
    """

    category: str
    change_percent: float


@dataclass
class Scenario:
    """
    A complete simulation scenario containing one or more changes.

    Attributes:
        scenario_id     Unique identifier for this scenario run.
        changes         List of ScenarioChange objects.
        horizon_months  Number of months to project forward.
    """

    scenario_id: str
    changes: List[ScenarioChange] = field(default_factory=list)
    horizon_months: int = 12
