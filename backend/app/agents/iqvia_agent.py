from app.agents.base import BaseAgent, llm
from app.schemas import AgentResult
from app.mock_data import mock_iqvia_data


class IQVIAAgent(BaseAgent):
    name = "IQVIA Insights Agent"

    def run(self, molecule: str, query: str) -> AgentResult:
        data = mock_iqvia_data(molecule)
        summary = llm.summarize(
            f"Summarize market size, growth and competition for {molecule}.",
            data,
        )
        # Simple score: bigger market + lower competitors = better
        markets = data["markets"]
        avg_size = sum(m["size"] for m in markets) / len(markets)
        avg_comp = sum(m["competitors"] for m in markets) / len(markets)
        score = min(100.0, (avg_size / 1_000_000) - avg_comp * 2)

        return AgentResult(
            agent_name=self.name,
            summary=summary,
            score=score,
            raw_data=data,
            references=[],
        )
