"""
simulation/projector.py — Monthly financial outcome projector.

Given a baseline and scenario changes, projects income, expenses,
and savings month-by-month over the simulation horizon.

TODO: Implement projection logic using numpy arrays.
TODO: Add seasonality adjustment based on historical monthly variance.
"""

from __future__ import annotations

from typing import List

import numpy as np

from app.schemas.simulation import ProjectedMonth
from app.simulation.scenario import Scenario


class Projector:
    """Projects monthly financial outcomes for a given scenario."""

    def project(
        self,
        scenario: Scenario,
        baseline_monthly_income: float,
        baseline_category_spend: dict[str, float],
    ) -> List[ProjectedMonth]:
        """
        Compute projected monthly outcomes for the scenario.

        Args:
            scenario:                   Simulation scenario with changes.
            baseline_monthly_income:    Average monthly income from history.
            baseline_category_spend:    Average monthly spend per category.

        Returns:
            List of ProjectedMonth with projected figures.

        TODO: Apply change_percent to each category in baseline_category_spend.
        TODO: Project forward for scenario.horizon_months.
        TODO: Construct ProjectedMonth list with month labels.
        """
        raise NotImplementedError("Projector.project not implemented.")
