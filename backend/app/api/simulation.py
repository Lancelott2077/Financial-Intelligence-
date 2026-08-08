"""
api/simulation.py — Counterfactual Simulation endpoint.

Accepts a behaviour ID and a proposed change (e.g., "reduce dining by 30%")
and returns a projected financial outcome over a given time horizon.

TODO: Implement via SimulationService.
TODO: Support multiple simultaneous scenario changes.
"""

from __future__ import annotations

from fastapi import APIRouter
from app.schemas.simulation import SimulationRequest, SimulationResponse

router = APIRouter()


@router.post(
    "/",
    response_model=SimulationResponse,
    summary="Run a counterfactual financial simulation",
)
async def run_simulation(request: SimulationRequest) -> SimulationResponse:
    """
    Execute a counterfactual simulation for a proposed behaviour change.
    """
    scenario_id = f"demo-{request.session_id[-8:]}"
    projected_months = [
        {"month": "2026-09", "projected_income": 12500.0, "projected_expenses": 9200.0, "projected_savings": 3300.0},
        {"month": "2026-10", "projected_income": 12500.0, "projected_expenses": 8900.0, "projected_savings": 3600.0},
        {"month": "2026-11", "projected_income": 12500.0, "projected_expenses": 8500.0, "projected_savings": 4000.0},
    ]
    return {
        "session_id": request.session_id,
        "scenario_id": scenario_id,
        "total_projected_saving": round(sum(m["projected_savings"] for m in projected_months), 2),
        "projected_months": projected_months,
        "summary": "Demo projection based on modest expense reductions and stable income.",
    }
