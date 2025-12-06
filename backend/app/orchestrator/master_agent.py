from typing import List, Tuple
from app.schemas import (
    UserQuery,
    AgentResult,
    FinalSynthesis,
)
from app.agents.iqvia_agent import IQVIAAgent
from app.agents.exim_agent import EXIMAgent
from app.agents.patent_agent import PatentAgent
from app.agents.trials_agent import TrialsAgent
from app.agents.internal_agent import InternalInsightsAgent
from app.agents.web_agent import WebIntelAgent
from app.agents.knowledge_graph_agent import KnowledgeGraphAgent
from app.agents.repurposing_agent import RepurposingAgent
from app.agents.toxicity_agent import ToxicityAgent
from app.agents.regulatory_agent import RegulatoryAgent
from app.agents.market_agent import MarketAgent
from app.agents.portfolio_agent import PortfolioOptimizerAgent
from app.agents.report_agent import ReportAgent
from app.services.scoring_engine import compute_scores_with_explanation
from app.services.memory_service import MemoryService


class MasterAgent:
    def __init__(self):
        self.iqvia = IQVIAAgent()
        self.exim = EXIMAgent()
        self.patent = PatentAgent()
        self.trials = TrialsAgent()
        self.internal = InternalInsightsAgent()
        self.web = WebIntelAgent()
        self.kg = KnowledgeGraphAgent()
        self.repurpose = RepurposingAgent()
        self.tox = ToxicityAgent()
        self.reg = RegulatoryAgent()
        self.market = MarketAgent()
        self.portfolio = PortfolioOptimizerAgent()
        self.report = ReportAgent()
        self.memory = MemoryService()

    def _extract_molecule(self, query: UserQuery) -> str:
        if query.molecule:
            return query.molecule
        for token in query.prompt.split():
            if token[0].isupper():
                return token.strip(",. ")
        return "Montelukast"

    def evaluate_once(self, query: UserQuery) -> Tuple[FinalSynthesis, str]:
        molecule = self._extract_molecule(query)

        agent_results: List[AgentResult] = []
        agent_results.append(self.iqvia.run(molecule, query.prompt))
        agent_results.append(self.exim.run(molecule, query.prompt))
        agent_results.append(self.patent.run(molecule, query.prompt))
        agent_results.append(self.trials.run(molecule, query.prompt))
        agent_results.append(self.internal.run(molecule, query.prompt))
        agent_results.append(self.web.run(molecule, query.prompt))
        agent_results.append(self.kg.run(molecule, query.prompt))
        rep = self.repurpose.run(molecule, query.prompt)
        agent_results.append(rep)
        agent_results.append(self.tox.run(molecule, query.prompt))
        agent_results.append(self.reg.run(molecule, query.prompt))
        agent_results.append(self.market.run(molecule, query.prompt))
        agent_results.append(self.portfolio.run(molecule, query.prompt))
        agent_results.append(self.report.run(molecule, query.prompt))

        scores, explanation = compute_scores_with_explanation(agent_results)
        recommended_indications = rep.raw_data.get("candidates", []) if rep.raw_data else []

        innovation_story = (
            f"For molecule {molecule}, the system identified high unmet need and attractive market "
            f"opportunities in: {', '.join(recommended_indications) or 'no strong new indications found yet'}. "
            f"Based on clinical evidence, market size, toxicity, patent and regulatory analysis, the "
            f"overall recommendation is: {scores.decision} (score={scores.overall_score:.1f})."
        )

        synthesis = FinalSynthesis(
            query=query,
            synthesis_text=innovation_story,
            agent_results=agent_results,
            scores=scores,
            innovation_story=innovation_story,
            recommended_indications=recommended_indications,
            explanation=explanation,
        )

        # Store in memory/history
        self.memory.add_entry(
            prompt=query.prompt,
            molecule=molecule,
            decision=scores.decision,
            overall_score=scores.overall_score,
        )

        report_id = self.report.generate_pdf(synthesis)
        return synthesis, report_id
