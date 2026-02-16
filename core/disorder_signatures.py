def detect_signatures(patient):

    mood = patient["mood_stability"]
    stress = patient["stress_level"]
    sleep = patient["sleep_quality"]
    anxiety = patient["anxiety_level"]
    variability = patient["symptom_variability"]
    adherence = patient["treatment_adherence"]
    support = patient["support_system"]

    signatures = []

    # 1️⃣ Anxiety Dominant
    if stress > 7 and anxiety > 7 and sleep < 5:
        signatures.append("Anxiety-Dominant State")

    # 2️⃣ Burnout Drift
    if stress > 7 and mood < 5 and adherence < 5:
        signatures.append("Burnout Drift Pattern")

    # 3️⃣ Depressive Collapse
    if mood < 4 and sleep < 5 and support < 5:
        signatures.append("Depressive Collapse Pattern")

    # 4️⃣ Cognitive Volatility 
    if variability > 7:
        signatures.append("Cognitive Volatility State")

    # 5️⃣ Resilience / Stability
    if (
        mood > 6
        and stress < 6
        and sleep > 5
        and anxiety < 6
        and variability < 6
    ):
        signatures.append("Resilient / Stable State")

    return signatures
