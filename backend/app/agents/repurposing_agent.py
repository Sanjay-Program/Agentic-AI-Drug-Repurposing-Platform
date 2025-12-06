from typing import List
from app.agents.base import BaseAgent, llm
from app.schemas import AgentResult
from app.mock_data import mock_disease_unmet_need, get_kg_graph


class RepurposingAgent(BaseAgent):
    name = "Repurposing Discovery Agent"

    def run(self, molecule: str, query: str) -> AgentResult:
        kg = get_kg_graph()
        unmet = mock_disease_unmet_need()

        # Choose diseases from KG + high unmet need + lower competition
        candidate_diseases: List[str] = []
        for row in unmet:
            d = row["disease"]
            if d in kg.nodes and row["unmet_need_score"] >= 70 and row["competition_score"] <= 60:
                candidate_diseases.append(d)

        data = {"candidates": candidate_diseases, "unmet": unmet}
        summary = llm.summarize(
            f"Suggest repurposing opportunities for {molecule} based on unmet need and KG.",
            data,
        )

        score = 90.0 if candidate_diseases else 55.0

        return AgentResult(
            agent_name=self.name,
            summary=summary,
            score=score,
            raw_data=data,
            references=[],
        )
