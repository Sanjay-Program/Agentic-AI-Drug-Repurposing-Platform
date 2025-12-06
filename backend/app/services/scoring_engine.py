from typing import List, Tuple
from app.schemas import AgentResult, ScoreBreakdown, ScoreContribution, Explanation


def compute_scores_with_explanation(
    agent_results: List[AgentResult],
) -> Tuple[ScoreBreakdown, Explanation]:
    def s(prefix: str) -> float:
        for r in agent_results:
            if r.agent_name.startswith(prefix):
                return r.score or 0.0
        return 0.0

    clinical = s("Clinical Trials Agent") + s("Web Intelligence Agent")
    clinical = min(100.0, clinical / 2)  # simple average

    market = s("IQVIA Insights Agent") + s("Market Attractiveness Agent")
    market = min(100.0, market / 2)

    competition = s("EXIM Trade Agent")
    toxicity = s("Toxicity Risk Agent")
    patent_risk = s("Patent Landscape Agent")
    regulatory = s("Regulatory Feasibility Agent")

    # Weights reflect importance
    w_clinical = 0.3
    w_market = 0.25
    w_competition = 0.1
    w_toxicity = 0.15
    w_patent = 0.1
    w_reg = 0.1

    overall = (
        w_clinical * clinical
        + w_market * market
        + w_competition * competition
        + w_toxicity * toxicity
        + w_patent * patent_risk
        + w_reg * regulatory
    )

    if overall >= 75:
        decision = "GO"
    elif overall >= 55:
        decision = "EXPLORE"
    else:
        decision = "NO_GO"

    scores = ScoreBreakdown(
        clinical_evidence_score=clinical,
        market_attractiveness_score=market,
        competition_score=competition,
        toxicity_score=toxicity,
        patent_risk_score=patent_risk,
        regulatory_feasibility_score=regulatory,
        overall_score=overall,
        decision=decision,
    )

    contributions = [
        ScoreContribution(
            dimension="Clinical Evidence",
            weight=w_clinical,
            contribution=w_clinical * clinical,
        ),
        ScoreContribution(
            dimension="Market Attractiveness",
            weight=w_market,
            contribution=w_market * market,
        ),
        ScoreContribution(
            dimension="Competition",
            weight=w_competition,
            contribution=w_competition * competition,
        ),
        ScoreContribution(
            dimension="Toxicity / Safety",
            weight=w_toxicity,
            contribution=w_toxicity * toxicity,
        ),
        ScoreContribution(
            dimension="Patent / FTO",
            weight=w_patent,
            contribution=w_patent * patent_risk,
        ),
        ScoreContribution(
            dimension="Regulatory Feasibility",
            weight=w_reg,
            contribution=w_reg * regulatory,
        ),
    ]

    explanation = Explanation(
        overall_score=overall, decision=decision, contributions=contributions
    )

    return scores, explanation
