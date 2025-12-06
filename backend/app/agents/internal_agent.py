from app.agents.base import BaseAgent, llm
from app.schemas import AgentResult
from app.mock_data import mock_internal_docs


class InternalInsightsAgent(BaseAgent):
    name = "Internal Knowledge Agent"

    def run(self, molecule: str, query: str) -> AgentResult:
        data = mock_internal_docs(molecule)
        summary = llm.summarize(
            f"Summarize internal strategy and field insights relevant to {molecule}.",
            data,
        )

        score = 75.0  # assume internal insights always valuable

        return AgentResult(
            agent_name=self.name,
            summary=summary,
            score=score,
            raw_data=data,
            references=[],
        )
