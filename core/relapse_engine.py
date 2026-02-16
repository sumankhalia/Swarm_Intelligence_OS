import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def compute_relapse_probability(patient, drift_metrics):
    """
    Predicts relapse probability using instability physics
    """

    stress_trend = drift_metrics["stress_level"]["trend"]
    anxiety_trend = drift_metrics["anxiety_level"]["trend"]
    sleep_trend = drift_metrics["sleep_quality"]["trend"]

    stress_vol = drift_metrics["stress_level"]["volatility"]
    anxiety_vol = drift_metrics["anxiety_level"]["volatility"]

    adherence = patient["treatment_adherence"]
    support = patient["support_system"]

    # 🔥 Relapse Pressure Equation
    relapse_pressure = (
        (stress_trend * 2.2)
        + (anxiety_trend * 2.0)
        - (sleep_trend * 1.8)
        + (stress_vol * 0.6)
        + (anxiety_vol * 0.6)
        - (adherence * 0.35)
        - (support * 0.25)
    )

    probability = sigmoid(relapse_pressure)

    return round(probability * 100, 2)


def interpret_relapse_risk(probability):
    """
    Converts probability into clinical language
    """

    if probability < 25:
        return "Low Relapse Risk"

    elif probability < 50:
        return "Moderate Relapse Vulnerability"

    elif probability < 75:
        return "High Relapse Risk Forming"

    else:
        return "Severe Relapse Probability – Preventive Intervention Recommended"
