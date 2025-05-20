from fastapi import APIRouter
from api.schemas import SimulationRequest

router = APIRouter()

@router.post("/start-simulation")
def start_simulation(sim: SimulationRequest):
    # Later: trigger simulation engine here
    return {
        "status": "received",
        "initial_investment": sim.initial_investment,
        "num_tests": sim.num_tests,
        "risk_tolerance": sim.risk_tolerance
    }
