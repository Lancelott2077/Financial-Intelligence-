"""schemas/simulation.py — Counterfactual Simulation Pydantic schemas."""

from __future__ import annotations

from typing import List
from pydantic import Field
from app.schemas.common import BaseResponse, SpendingCategory


class ScenarioChange(BaseResponse):
    """A single behaviour change to simulate."""

    category: SpendingCategory = Field(description="Spending category to modify.")
    change_percent: float = Field(
        ge=-100.0,
        le=100.0,
        description="Percentage change (negative = reduction).",
    )


class ProjectedMonth(BaseResponse):
    """Projected financials for one month in the simulation."""

    month: str
    projected_income: float
    projected_expenses: float
    projected_savings: float


class SimulationRequest(BaseResponse):
    """Request body for a counterfactual simulation run."""

    session_id: str
    behaviour_id: int | None = None
    scenario_changes: List[ScenarioChange] = Field(
        default_factory=list
    )
    horizon_months: int = Field(default=12, ge=1, le=60)


class SimulationResponse(BaseResponse):
    """
    Results of a counterfactual simulation.

    TODO: Populate from SimulationService.run().
    """

    session_id: str
    scenario_id: str
    total_projected_saving: float = 0.0
    projected_months: List[ProjectedMonth] = Field(default_factory=list)
    summary: str = ""
