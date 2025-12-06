from typing import List
from app.schemas import SignalEvent, SignalsResponse
from app.mock_data import mock_trials_data, mock_patent_data, mock_toxicity_data, mock_web_results


class SignalsService:
    def get_signals_for_molecule(self, molecule: str) -> SignalsResponse:
        trials = mock_trials_data(molecule)
        patents = mock_patent_data(molecule)
        tox = mock_toxicity_data(molecule)
        web = mock_web_results(molecule)

        signals: List[SignalEvent] = []

        # Trial signal
        for t in trials.get("trials", []):
            if t["status"].lower() in ("recruiting", "active"):
                signals.append(
                    SignalEvent(
                        category="trials",
                        title=f"Active trial in {t['indication']} ({t['phase']})",
                        description=f"Trial {t['id']} is {t['status']}.",
                        severity="medium",
                    )
                )

        # Patent signal
        for p in patents.get("patents", []):
            if p["expiry_year"] <= 2028:
                signals.append(
                    SignalEvent(
                        category="patent",
                        title=f"Patent {p['patent_id']} nearing expiry",
                        description=f"Owned by {p['owner']}, expires {p['expiry_year']}.",
                        severity="medium",
                    )
                )

        # Safety signal
        if tox.get("black_box_warning"):
            signals.append(
                SignalEvent(
                    category="safety",
                    title="Black box warning detected",
                    description=f"{molecule} has a regulatory black box warning.",
                    severity="high",
                )
            )

        # Guideline/news
        for g in web.get("guidelines", []):
            signals.append(
                SignalEvent(
                    category="guideline",
                    title=f"Guideline update: {g['source']}",
                    description=g["snippet"],
                    severity="low",
                )
            )
        for n in web.get("news", []):
            signals.append(
                SignalEvent(
                    category="news",
                    title=n["headline"],
                    description="News relevant to potential repurposing.",
                    severity="low",
                    link=n["url"],
                )
            )

        return SignalsResponse(molecule=molecule, signals=signals)
