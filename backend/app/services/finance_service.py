import math
from app.schemas import ScenarioParams, ScenarioResult


class FinanceService:
    def simulate(self, params: ScenarioParams) -> ScenarioResult:
        # Adjusted score based on market growth and competition deltas:
        score_adjust = params.market_growth_delta * 1.0 - params.competition_delta * 1.0
        adjusted_score = max(0.0, min(100.0, params.base_overall_score + score_adjust))

        # Simple NPV: assume ramp-up to peak over years_to_peak, then flat until patent end
        cashflows = []
        t = 0
        for year in range(1, params.years_to_peak + 1):
            t += 1
            cf = params.peak_sales_musd * (year / params.years_to_peak)
            cashflows.append(cf)
        for year in range(params.years_to_peak + 1, params.patent_years_left + 1):
            t += 1
            cashflows.append(params.peak_sales_musd)

        # initial dev cost
        npv = -params.dev_cost_musd
        for i, cf in enumerate(cashflows):
            npv += cf / ((1 + params.discount_rate) ** (i + 1))

        # crude payback: when cumulative CF > dev cost
        cum = 0.0
        payback_years = None
        for i, cf in enumerate(cashflows):
            cum += cf
            if cum >= params.dev_cost_musd:
                payback_years = i + 1
                break
        if payback_years is None:
            payback_years = float("inf")

        comment = (
            f"Adjusted innovation score: {adjusted_score:.1f}. "
            f"NPV ≈ {npv:.1f} MUSD, payback in "
            f"{'>' if math.isinf(payback_years) else ''}{payback_years if not math.isinf(payback_years) else ''} years."
        )

        return ScenarioResult(
            adjusted_score=adjusted_score,
            npv_musd=npv,
            payback_years=payback_years,
            comment=comment,
        )
