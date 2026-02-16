import random

def generate_patient():
    return {
        "mood_stability": random.uniform(1, 10),
        "stress_level": random.uniform(1, 10),
        "sleep_quality": random.uniform(1, 10),
        "anxiety_level": random.uniform(1, 10),
        "symptom_variability": random.uniform(1, 10),
        "treatment_adherence": random.uniform(1, 10),
        "support_system": random.uniform(1, 10),
    }
