def strategy_score(p):
    return (
        p["mood_stability"] * 0.35
        + p["sleep_quality"] * 0.25
        + p["treatment_adherence"] * 0.40
    )


def risk_score(p):
    return (
        p["stress_level"] * 0.40
        + p["anxiety_level"] * 0.40
        + p["symptom_variability"] * 0.20
    )


def governance_score(p):
    return (
        p["support_system"] * 0.60
        + p["treatment_adherence"] * 0.40
    )


def skeptic_pressure(strategy, risk):
    return abs(strategy - risk)


def composite_score(strategy, risk, governance, skeptic):
    return (strategy * 0.4) - (risk * 0.4) + (governance * 0.2) - (skeptic * 0.3)


def executive_decision(score):

    if score > 2:
        return "Stable / Resilient State"

    elif score > 0:
        return "Inconclusive – Gather More Data"

    else:
        return "High Risk – Clinical Attention Recommended"


def confidence_score(score):
    base = 50 + (score * 10)
    return max(0, min(100, round(base, 2)))
