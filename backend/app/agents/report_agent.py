from app.agents.base import BaseAgent
from app.schemas import AgentResult, FinalSynthesis
from app.services.pdf_report import PdfReportService


class ReportAgent(BaseAgent):
    name = "Report Generator Agent"

    def __init__(self):
        self.pdf_service = PdfReportService()

    def run(self, molecule: str, query: str) -> AgentResult:
        # Not used directly; MasterAgent will call pdf_service with FinalSynthesis.
        summary = (
            "Formats synthesized response into a polished PDF report, including charts, tables, "
            "and references. In this architecture, this agent is used indirectly via MasterAgent."
        )
        return AgentResult(
            agent_name=self.name,
            summary=summary,
            score=None,
            raw_data={},
            references=[],
        )

    def generate_pdf(self, synthesis: FinalSynthesis) -> str:
        return self.pdf_service.generate_report(synthesis)
