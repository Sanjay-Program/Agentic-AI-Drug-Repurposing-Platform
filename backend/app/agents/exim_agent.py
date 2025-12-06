from app.agents.base import BaseAgent, llm
from app.schemas import AgentResult
from app.mock_data import mock_exim_data


class EXIMAgent(BaseAgent):
    name = "EXIM Trade Agent"

    def run(self, molecule: str, query: str) -> AgentResult:
        data = mock_exim_data(molecule)
        summary = llm.summarize(
            f"Summarize API trade flows and supply chain risk for {molecule}.",
            data,
        )
        total_volume = sum(f["volume_tons"] for f in data["trade_flows"])
        # More diversified = lower risk → higher score
        unique_routes = len({(f["from"], f["to"]) for f in data["trade_flows"]})
        score = min(100.0, 50 + unique_routes * 10)

        return AgentResult(
            agent_name=self.name,
            summary=summary,
            score=score,
            raw_data=data,
            references=[],
        )
