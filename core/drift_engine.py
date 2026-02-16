import numpy as np


def compute_drift(timeline):
    """
    Measures psychological drift over time
    """

    drift_metrics = {}

    for key in timeline[0].keys():

        values = [month[key] for month in timeline]

        slope = np.polyfit(range(len(values)), values, 1)[0]

        volatility = np.std(values)

        drift_metrics[key] = {
            "trend": round(slope, 3),
            "volatility": round(volatility, 3)
        }

    return drift_metrics


def detect_instability(drift_metrics):
    """
    Detects emerging mental instability
    """

    warnings = []

    for signal, metrics in drift_metrics.items():

        trend = metrics["trend"]
        volatility = metrics["volatility"]

        # Instability Logic
        if trend > 0.25 and signal in ["stress_level", "anxiety_level"]:
            warnings.append(f"Rising {signal}")

        if trend < -0.25 and signal == "sleep_quality":
            warnings.append("Sleep deterioration")

        if volatility > 1.8:
            warnings.append(f"High volatility in {signal}")

    if not warnings:
        return "Stable Cognitive Pattern"

    return warnings
