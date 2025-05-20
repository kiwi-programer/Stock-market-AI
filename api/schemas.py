from pydantic import BaseModel, Field
from typing import Literal

class SimulationRequest(BaseModel):
    initial_investment: float = Field(..., gt=0, description="Starting money in USD")
    num_tests: int = Field(..., gt=0, description="Number of simulations to run")
    risk_tolerance: Literal["low", "medium", "high"] = Field(..., description="Risk level")
