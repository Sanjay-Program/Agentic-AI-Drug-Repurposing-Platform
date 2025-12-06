from app.agents.base import BaseAgent, llm
from app.schemas import AgentResult
from app.mock_data import mock_regulatory_data


class RegulatoryAgent(BaseAgent):
    name = "Regulatory Feasibility Agent"

    def run(self, molecule: str, query: str) -> AgentResult:
        data = mock_regulatory_data(molecule)
        summary = llm.summarize(
            f"Assess regulatory feasibility and fast-track potential for {molecule}.",
            data,
        )

        approvals = data.get("approvals", [])
        fast_track = data.get("fast_track_potential", [])
        score = 70.0 + 10.0 * len(fast_track)
        if not approvals:
            score -= 20.0

        return AgentResult(
            agent_name=self.name,
            summary=summary,
            score=score,
            raw_data=data,
            references=[],
        )
