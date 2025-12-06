from fastapi import APIRouter, HTTPException
from app.schemas import (
    UserQuery,
    EvaluationResponse,
    BatchEvaluationRequest,
    BatchEvaluationResponse,
    MoleculeEvaluationSummary,
)
from app.orchestrator.master_agent import MasterAgent

router = APIRouter()
master = MasterAgent()


@router.post("/", response_model=EvaluationResponse)
def evaluate_query(query: UserQuery):
    if not query.prompt:
        raise HTTPException(status_code=400, detail="prompt is required")
    synthesis, report_id = master.evaluate_once(query)
    return EvaluationResponse(synthesis=synthesis, report_id=report_id)


@router.post("/batch", response_model=BatchEvaluationResponse)
def evaluate_batch(req: BatchEvaluationRequest):
    summaries: list[MoleculeEvaluationSummary] = []
    for item in req.items:
        q = UserQuery(
            prompt=item.prompt,
            molecule=item.molecule,
            target_diseases=item.target_diseases,
        )
        synthesis, _ = master.evaluate_once(q)
        s = synthesis.scores
        summaries.append(
            MoleculeEvaluationSummary(
                molecule=item.molecule,
                decision=s.decision,
                overall_score=s.overall_score,
                clinical_evidence_score=s.clinical_evidence_score,
                market_attractiveness_score=s.market_attractiveness_score,
                toxicity_score=s.toxicity_score,
                patent_risk_score=s.patent_risk_score,
                regulatory_feasibility_score=s.regulatory_feasibility_score,
            )
        )
    return BatchEvaluationResponse(items=summaries)
