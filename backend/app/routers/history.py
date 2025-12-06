from fastapi import APIRouter
from app.schemas import HistoryResponse
from app.services.memory_service import MemoryService

router = APIRouter()
memory = MemoryService()


@router.get("/", response_model=HistoryResponse)
def get_history():
    items = memory.list_entries()
    return HistoryResponse(items=items)
