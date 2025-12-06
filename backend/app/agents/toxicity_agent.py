from app.agents.base import BaseAgent, llm
from app.schemas import AgentResult
from app.mock_data import mock_toxicity_data


class ToxicityAgent(BaseAgent):
    name = "Toxicity Risk Agent"

    def run(self, molecule: str, query: str) -> AgentResult:
        data = mock_toxicity_data(molecule)
        summary = llm.summarize(
            f"Summarize toxicity and safety profile of {molecule}.",
            data,
        )

        # crude scoring
        has_black_box = data["black_box_warning"]
        base_score = 85.0
        if has_black_box:
            base_score -= 40.0

        score = base_score

        return AgentResult(
            agent_name=self.name,
            summary=summary,
            score=score,
            raw_data=data,
            references=[],
        )
