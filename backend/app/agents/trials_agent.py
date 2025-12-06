from app.agents.base import BaseAgent, llm
from app.schemas import AgentResult
from app.mock_data import mock_trials_data


class TrialsAgent(BaseAgent):
    name = "Clinical Trials Agent"

    def run(self, molecule: str, query: str) -> AgentResult:
        data = mock_trials_data(molecule)
        summary = llm.summarize(
            f"Summarize ongoing and completed trials for {molecule}. "
            "Highlight trial density and competition.",
            data,
        )

        trials = data["trials"]
        # More trials = more evidence but also more competition; keep mid
        trial_count = len(trials)
        score = min(100.0, 60 + trial_count * 5)

        return AgentResult(
            agent_name=self.name,
            summary=summary,
            score=score,
            raw_data=data,
            references=[],
        )
