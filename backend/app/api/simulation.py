"""
api/simulation.py — Counterfactual Simulation endpoint.

Accepts a behaviour ID and a proposed change (e.g., "reduce dining by 30%")
and returns a projected financial outcome over a given time horizon.

TODO: Implement via SimulationService.
TODO: Support multiple simultaneous scenario changes.
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException, status
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

    TODO: Validate session_id and behaviour_id.
    TODO: Call SimulationService.run(request).
    TODO: Return SimulationResponse with projected outcomes.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Simulation endpoint not yet implemented.",
    )
