from fastapi import APIRouter
from app.schemas import ScenarioParams, ScenarioResult
from app.services.finance_service import FinanceService

router = APIRouter()
finance = FinanceService()


@router.post("/simulate", response_model=ScenarioResult)
def simulate_scenario(params: ScenarioParams):
    return finance.simulate(params)
