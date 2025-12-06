from app.agents.base import BaseAgent, llm
from app.schemas import AgentResult
from app.mock_data import mock_iqvia_data


class MarketAgent(BaseAgent):
    name = "Market Attractiveness Agent"

    def run(self, molecule: str, query: str) -> AgentResult:
        data = mock_iqvia_data(molecule)
        summary = llm.summarize(
            f"Evaluate commercial attractiveness and revenue potential for {molecule}.",
            data,
        )

        markets = data["markets"]
        total_size = sum(m["size"] for m in markets)
        avg_cagr = sum(m["cagr"] for m in markets) / len(markets)
        score = min(100.0, (total_size / 1_000_000) * 0.5 + avg_cagr)

        return AgentResult(
            agent_name=self.name,
            summary=summary,
            score=score,
            raw_data=data,
            references=[],
        )
