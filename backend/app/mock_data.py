from typing import Dict, Any, List
import networkx as nx

# Simple synthetic DBs. In real setup load from JSON/CSV.


def mock_iqvia_data(molecule: str) -> Dict[str, Any]:
    return {
        "molecule": molecule,
        "markets": [
            {"region": "US", "therapy": "Asthma", "size": 500_000_000, "cagr": 8.5, "competitors": 5},
            {"region": "India", "therapy": "Asthma", "size": 120_000_000, "cagr": 11.0, "competitors": 2},
        ],
    }


def mock_exim_data(molecule: str) -> Dict[str, Any]:
    return {
        "molecule": molecule,
        "trade_flows": [
            {"api": molecule, "from": "China", "to": "India", "volume_tons": 250},
            {"api": molecule, "from": "India", "to": "US", "volume_tons": 100},
        ],
    }


def mock_patent_data(molecule: str) -> Dict[str, Any]:
    return {
        "molecule": molecule,
        "patents": [
            {"patent_id": "US1234567A", "owner": "BigPharma Inc", "expiry_year": 2028, "fto_risk": "medium"},
            {"patent_id": "US7654321B", "owner": "GenericCo", "expiry_year": 2026, "fto_risk": "low"},
        ],
    }


def mock_trials_data(molecule: str) -> Dict[str, Any]:
    return {
        "molecule": molecule,
        "trials": [
            {"id": "NCT001", "indication": "Asthma", "phase": "Phase III", "status": "Completed"},
            {"id": "NCT002", "indication": "COPD", "phase": "Phase II", "status": "Recruiting"},
        ],
    }


def mock_internal_docs(molecule: str) -> Dict[str, Any]:
    return {
        "molecule": molecule,
        "docs": [
            {"title": "Field Insights - Respiratory 2024", "key_points": ["High unmet need in chronic cough", "Poor adherence in inhaler users"]},
            {"title": "Strategy Deck - Emerging Markets", "key_points": ["India Tier-2 cities growth", "Price-sensitive but volume rich"]},
        ],
    }


def mock_web_results(molecule: str) -> Dict[str, Any]:
    return {
        "molecule": molecule,
        "guidelines": [
            {"source": "GINA", "snippet": f"{molecule} is recommended as add-on therapy in persistent asthma."},
        ],
        "news": [
            {"headline": f"New studies explore {molecule} in chronic cough", "url": "https://example.com/news1"},
        ],
    }


def mock_toxicity_data(molecule: str) -> Dict[str, Any]:
    return {
        "molecule": molecule,
        "adverse_events": [
            {"event": "Headache", "frequency": "very common"},
            {"event": "Neuropsychiatric effects", "frequency": "rare"},
        ],
        "black_box_warning": False,
    }


def mock_regulatory_data(molecule: str) -> Dict[str, Any]:
    return {
        "molecule": molecule,
        "approvals": [
            {"agency": "FDA", "indication": "Asthma", "year": 1998},
            {"agency": "EMA", "indication": "Asthma", "year": 1999},
        ],
        "fast_track_potential": ["Chronic cough"],
        "orphan_potential": [],
    }


def mock_disease_unmet_need() -> List[Dict[str, Any]]:
    return [
        {"disease": "Chronic cough", "prevalence": "high", "unmet_need_score": 90, "competition_score": 30},
        {"disease": "COPD", "prevalence": "high", "unmet_need_score": 70, "competition_score": 60},
        {"disease": "Allergic rhinitis", "prevalence": "medium", "unmet_need_score": 50, "competition_score": 50},
    ]


# Knowledge graph: Drug → MoA → Pathway → Disease, etc.
_KG_GRAPH = nx.MultiDiGraph()
_KG_BUILT = False


def _build_kg():
    global _KG_BUILT
    if _KG_BUILT:
        return

    drug = "Montelukast"
    _KG_GRAPH.add_node(drug, type="drug")
    _KG_GRAPH.add_node("Leukotriene receptor antagonist", type="moa")
    _KG_GRAPH.add_node("Inflammatory pathway", type="pathway")
    _KG_GRAPH.add_node("Asthma", type="disease")
    _KG_GRAPH.add_node("Chronic cough", type="disease")
    _KG_GRAPH.add_node("Allergic rhinitis", type="disease")

    _KG_GRAPH.add_edge(drug, "Leukotriene receptor antagonist", type="has_moa")
    _KG_GRAPH.add_edge("Leukotriene receptor antagonist", "Inflammatory pathway", type="acts_on")
    _KG_GRAPH.add_edge("Inflammatory pathway", "Asthma", type="implicated_in")
    _KG_GRAPH.add_edge("Inflammatory pathway", "Chronic cough", type="implicated_in")
    _KG_GRAPH.add_edge("Inflammatory pathway", "Allergic rhinitis", type="implicated_in")

    _KG_BUILT = True


def get_kg_graph() -> nx.MultiDiGraph:
    _build_kg()
    return _KG_GRAPH
