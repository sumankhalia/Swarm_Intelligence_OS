import random


def bounded(val):
    return max(1, min(10, round(val, 2)))


def generate_patient():

    stress = random.uniform(3, 9)
    anxiety = stress + random.uniform(-2, 2)

    sleep = 10 - stress + random.uniform(-2, 2)
    mood = sleep + random.uniform(-2, 2)

    adherence = random.uniform(1, 9)
    support = random.uniform(2, 9)

    variability = (stress + anxiety) / 4 + random.uniform(-1.5, 1.5)

    return {
        "mood_stability": bounded(mood),
        "stress_level": bounded(stress),
        "anxiety_level": bounded(anxiety),
        "sleep_quality": bounded(sleep),
        "symptom_variability": bounded(variability),
        "treatment_adherence": bounded(adherence),
        "support_system": bounded(support),
    }
