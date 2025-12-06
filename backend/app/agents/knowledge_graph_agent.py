from app.agents.base import BaseAgent, llm
from app.schemas import AgentResult
from app.mock_data import get_kg_graph


class KnowledgeGraphAgent(BaseAgent):
    name = "Knowledge Graph Agent"

    def run(self, molecule: str, query: str) -> AgentResult:
        graph = get_kg_graph()

        if molecule not in graph:
            summary = f"No knowledge graph data found for {molecule}."
            return AgentResult(
                agent_name=self.name,
                summary=summary,
                score=40.0,
                raw_data={},
                references=[],
            )

        neighbors = list(graph.neighbors(molecule))
        diseases = [n for n in neighbors if graph.nodes[n].get("type") == "disease"]

        data = {
            "nodes": list(graph.nodes(data=True)),
            "edges": list(graph.edges(data=True)),
            "disease_neighbors": diseases,
        }

        summary = llm.summarize(
            f"Analyze knowledge graph around {molecule} and list related diseases.",
            data,
        )

        score = 85.0 if diseases else 60.0

        return AgentResult(
            agent_name=self.name,
            summary=summary,
            score=score,
            raw_data=data,
            references=[],
        )
