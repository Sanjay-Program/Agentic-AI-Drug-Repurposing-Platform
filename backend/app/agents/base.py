from abc import ABC, abstractmethod
from typing import Dict, Any
from app.schemas import AgentResult


class BaseAgent(ABC):
    name: str

    @abstractmethod
    def run(self, molecule: str, query: str) -> AgentResult:
        ...


class DummyLLM:
    """Simple stub to simulate LLM summarization."""

    def summarize(self, instruction: str, data: Dict[str, Any]) -> str:
        return f"{instruction}\n\nKey data: {str(data)[:400]}..."


llm = DummyLLM()
