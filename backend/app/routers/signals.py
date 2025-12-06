from fastapi import APIRouter, Query
from app.schemas import SignalsResponse
from app.services.signals_service import SignalsService

router = APIRouter()
signals_service = SignalsService()


@router.get("/", response_model=SignalsResponse)
def get_signals(molecule: str = Query("Montelukast")):
    return signals_service.get_signals_for_molecule(molecule)
