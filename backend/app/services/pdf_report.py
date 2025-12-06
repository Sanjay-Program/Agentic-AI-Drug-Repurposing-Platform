import os
import uuid
from typing import List
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from app.schemas import FinalSynthesis, AgentResult, ScoreBreakdown, UserQuery

REPORT_DIR = os.path.join(os.path.dirname(__file__), "..", "archive", "reports")


class PdfReportService:
    def __init__(self):
        os.makedirs(REPORT_DIR, exist_ok=True)

    def generate_report(self, synthesis: FinalSynthesis) -> str:
        report_id = str(uuid.uuid4())
        pdf_path = os.path.join(REPORT_DIR, f"{report_id}.pdf")

        styles = getSampleStyleSheet()
        story = []

        q: UserQuery = synthesis.query
        scores: ScoreBreakdown = synthesis.scores
        agents: List[AgentResult] = synthesis.agent_results

        story.append(Paragraph("Drug Repurposing Innovation Report", styles["Title"]))
        story.append(Spacer(1, 12))
        story.append(Paragraph(f"Prompt: {q.prompt}", styles["Normal"]))
        story.append(Spacer(1, 12))

        story.append(Paragraph("Overall Decision & Scores", styles["Heading2"]))
        story.append(
            Paragraph(
                f"<b>Decision:</b> {scores.decision}<br/>"
                f"Overall Score: {scores.overall_score:.1f}<br/>"
                f"Clinical Evidence: {scores.clinical_evidence_score:.1f}<br/>"
                f"Market Attractiveness: {scores.market_attractiveness_score:.1f}<br/>"
                f"Competition: {scores.competition_score:.1f}<br/>"
                f"Toxicity: {scores.toxicity_score:.1f}<br/>"
                f"Patent Risk: {scores.patent_risk_score:.1f}<br/>"
                f"Regulatory Feasibility: {scores.regulatory_feasibility_score:.1f}",
                styles["Normal"],
            )
        )
        story.append(Spacer(1, 12))

        story.append(Paragraph("Innovation Story", styles["Heading2"]))
        story.append(Paragraph(synthesis.innovation_story, styles["Normal"]))
        story.append(Spacer(1, 12))

        if synthesis.recommended_indications:
            story.append(Paragraph("Recommended Repurposing Indications", styles["Heading2"]))
            story.append(
                Paragraph(", ".join(synthesis.recommended_indications), styles["Normal"])
            )
            story.append(Spacer(1, 12))

        story.append(Paragraph("Agent Insights", styles["Heading2"]))
        for r in agents:
            story.append(Paragraph(f"<b>{r.agent_name}</b>", styles["Heading3"]))
            story.append(Paragraph(r.summary, styles["Normal"]))
            story.append(Spacer(1, 6))

        doc = SimpleDocTemplate(pdf_path, pagesize=A4)
        doc.build(story)

        return report_id

    def get_report_path(self, report_id: str) -> str | None:
        path = os.path.join(REPORT_DIR, f"{report_id}.pdf")
        return path if os.path.exists(path) else None
