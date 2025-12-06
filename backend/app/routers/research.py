from fastapi import APIRouter
from app.schemas import AutoResearchResponse, AutoResearchResponseItem, UserQuery
from app.orchestrator.master_agent import MasterAgent

router = APIRouter()
master = MasterAgent()


@router.get("/auto", response_model=AutoResearchResponse)
def auto_research():
    # Simple synthetic candidate list for demo
    candidates = [
        ("Montelukast", "Evaluate Montelukast for respiratory repurposing opportunities"),
        ("DrugX", "Evaluate DrugX for high unmet need in respiratory indications"),
        ("DrugY", "Evaluate DrugY for chronic cough and COPD opportunities"),
    ]

    items: list[AutoResearchResponseItem] = []
    for mol, prompt in candidates:
        q = UserQuery(prompt=prompt, molecule=mol, target_diseases=["Asthma", "Chronic cough"])
        synthesis, _ = master.evaluate_once(q)
        items.append(
            AutoResearchResponseItem(
                molecule=mol,
                decision=synthesis.scores.decision,
                overall_score=synthesis.scores.overall_score,
                recommended_indications=synthesis.recommended_indications,
            )
        )

    # sort by score descending
    items.sort(key=lambda x: x.overall_score, reverse=True)
    return AutoResearchResponse(items=items)
