from app.agents.base import BaseAgent, llm
from app.schemas import AgentResult
from app.mock_data import mock_patent_data


class PatentAgent(BaseAgent):
    name = "Patent Landscape Agent"

    def run(self, molecule: str, query: str) -> AgentResult:
        data = mock_patent_data(molecule)
        summary = llm.summarize(
            f"Summarize patent filings, expiry timeline and FTO risks for {molecule}.",
            data,
        )
        patents = data["patents"]
        # Lower FTO risk and nearer expiry = better
        avg_expiry = sum(p["expiry_year"] for p in patents) / len(patents)
        base = 80 if any(p["fto_risk"] == "low" for p in patents) else 50
        score = max(10.0, base - (avg_expiry - 2025) * 5)

        return AgentResult(
            agent_name=self.name,
            summary=summary,
            score=score,
            raw_data=data,
            references=[],
        )
