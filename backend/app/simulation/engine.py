"""
simulation/engine.py — Core counterfactual simulation engine.

Takes a SimulationRequest and historical transaction data to compute
projected financial outcomes over a specified time horizon.

TODO: Implement simulation computation using numpy.
TODO: Support compound effects across multiple scenario changes.
TODO: Add Monte Carlo uncertainty bands.
"""

from __future__ import annotations

import uuid
from typing import List

import numpy as np
import pandas as pd

from app.schemas.simulation import (
    SimulationRequest,
    SimulationResponse,
    ProjectedMonth,
)


class SimulationEngine:
    """Computes counterfactual financial projections."""

    async def run(
        self, request: SimulationRequest, historical_df: pd.DataFrame
    ) -> SimulationResponse:
        """
        Execute a counterfactual simulation.

        Args:
            request:        SimulationRequest with scenario_changes and horizon.
            historical_df:  Historical transaction DataFrame for the session.

        Returns:
            SimulationResponse with projected monthly outcomes.

        TODO: Compute baseline monthly averages from historical_df.
        TODO: Apply each ScenarioChange as a percentage modifier to its category.
        TODO: Project forward for horizon_months using numpy.
        TODO: Accumulate total_projected_saving.
        TODO: Construct ProjectedMonth list.
        """
        raise NotImplementedError("SimulationEngine.run not implemented.")
