from data.synthetic_data import generate_patient
from core.time_evolution import evolve_patient
from core.disorder_signatures import apply_anxiety_signature
import random

def simulate_population(size=1000, months=12):

    population = [generate_patient() for _ in range(size)]

    history = []

    for month in range(months):

        month_snapshot = []

        for patient in population:

            patient = evolve_patient(patient)

            if random.random() < 0.25:   # disorder probability
                patient = apply_anxiety_signature(patient)

            month_snapshot.append(patient.copy())

        history.append(month_snapshot)

    return history
