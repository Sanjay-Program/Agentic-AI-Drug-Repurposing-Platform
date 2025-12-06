from pydantic import BaseModel
from typing import List, Dict, Optional, Any


class UserQuery(BaseModel):
    prompt: str
    molecule: Optional[str] = None
    target_diseases: List[str] = []


class AgentResult(BaseModel):
    agent_name: str
    summary: str
    score: Optional[float] = None
    raw_data: Dict[str, Any] = {}
    references: List[str] = []


class ScoreBreakdown(BaseModel):
    clinical_evidence_score: float
    market_attractiveness_score: float
    competition_score: float
    toxicity_score: float
    patent_risk_score: float
    regulatory_feasibility_score: float
    overall_score: float
    decision: str  # GO / EXPLORE / NO_GO


class ScoreContribution(BaseModel):
    dimension: str
    weight: float
    contribution: float


class Explanation(BaseModel):
    overall_score: float
    decision: str
    contributions: List[ScoreContribution]


class FinalSynthesis(BaseModel):
    query: UserQuery
    synthesis_text: str
    agent_results: List[AgentResult]
    scores: ScoreBreakdown
    innovation_story: str
    recommended_indications: List[str]
    explanation: Explanation


class EvaluationResponse(BaseModel):
    synthesis: FinalSynthesis
    report_id: str


# Batch / portfolio evaluation

class MoleculeQuery(BaseModel):
    molecule: str
    prompt: str
    target_diseases: List[str] = []


class BatchEvaluationRequest(BaseModel):
    items: List[MoleculeQuery]


class MoleculeEvaluationSummary(BaseModel):
    molecule: str
    decision: str
    overall_score: float
    clinical_evidence_score: float
    market_attractiveness_score: float
    toxicity_score: float
    patent_risk_score: float
    regulatory_feasibility_score: float


class BatchEvaluationResponse(BaseModel):
    items: List[MoleculeEvaluationSummary]


# History / memory

class HistoryEntry(BaseModel):
    id: str
    prompt: str
    molecule: Optional[str]
    decision: str
    overall_score: float


class HistoryResponse(BaseModel):
    items: List[HistoryEntry]


# Scenario & ROI simulation

class ScenarioParams(BaseModel):
    molecule: str
    base_overall_score: float
    dev_cost_musd: float  # development cost in million USD
    peak_sales_musd: float  # estimated peak annual sales (MUSD)
    years_to_peak: int
    patent_years_left: int
    discount_rate: float = 0.1  # 10% default
    market_growth_delta: float = 0.0  # +/- percentage points
    competition_delta: float = 0.0  # +/- effect on score


class ScenarioResult(BaseModel):
    adjusted_score: float
    npv_musd: float
    payback_years: float
    comment: str


# Signals

class SignalEvent(BaseModel):
    category: str  # "trials", "patent", "safety", "guideline"
    title: str
    description: str
    severity: str  # low / medium / high
    link: Optional[str] = None


class SignalsResponse(BaseModel):
    molecule: str
    signals: List[SignalEvent]


# Auto research (autonomous mode)

class AutoResearchResponseItem(BaseModel):
    molecule: str
    decision: str
    overall_score: float
    recommended_indications: List[str]


class AutoResearchResponse(BaseModel):
    items: List[AutoResearchResponseItem]
