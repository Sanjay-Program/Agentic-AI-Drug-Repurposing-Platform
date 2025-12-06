import os
import json
import uuid
from typing import List
from app.schemas import HistoryEntry


MEMORY_DIR = os.path.join(os.path.dirname(__file__), "..", "archive")
MEMORY_FILE = os.path.join(MEMORY_DIR, "history.json")


class MemoryService:
    def __init__(self):
        os.makedirs(MEMORY_DIR, exist_ok=True)
        if not os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "w", encoding="utf-8") as f:
                json.dump([], f)

    def _load(self) -> List[dict]:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save(self, items: List[dict]) -> None:
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(items, f, indent=2)

    def add_entry(
        self, prompt: str, molecule: str | None, decision: str, overall_score: float
    ) -> HistoryEntry:
        items = self._load()
        entry_id = str(uuid.uuid4())
        entry = {
            "id": entry_id,
            "prompt": prompt,
            "molecule": molecule,
            "decision": decision,
            "overall_score": overall_score,
        }
        items.append(entry)
        self._save(items)
        return HistoryEntry(**entry)

    def list_entries(self, limit: int = 50) -> List[HistoryEntry]:
        items = self._load()
        items = items[-limit:]
        return [HistoryEntry(**item) for item in items]
