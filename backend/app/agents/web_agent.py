from app.agents.base import BaseAgent, llm
from app.schemas import AgentResult
from app.mock_data import mock_web_results


class WebIntelAgent(BaseAgent):
    name = "Web Intelligence Agent"

    def run(self, molecule: str, query: str) -> AgentResult:
        data = mock_web_results(molecule)
        summary = llm.summarize(
            f"Summarize guidelines, scientific publications and news for {molecule}.",
            data,
        )
        score = 80.0  # assume good web evidence for demo

        refs = [g.get("source", "") for g in data.get("guidelines", [])]
        refs += [n.get("url", "") for n in data.get("news", [])]

        return AgentResult(
            agent_name=self.name,
            summary=summary,
            score=score,
            raw_data=data,
            references=refs,
        )
