import random
import copy


def clamp(value, low=1, high=10):
    return max(low, min(high, value))


def evolve_patient(patient, months=12):
    """
    Simulates patient psychological evolution over time
    """

    history = []
    state = copy.deepcopy(patient)

    for month in range(months):

        # 🔥 Random life stress shocks
        stress_shock = random.uniform(-0.8, 1.2)

        # Stress dynamics
        state["stress_level"] = clamp(
            state["stress_level"] + stress_shock
        )

        # Anxiety reacts to stress
        anxiety_drift = (state["stress_level"] - 5) * 0.15
        state["anxiety_level"] = clamp(
            state["anxiety_level"] + anxiety_drift
        )

        # Sleep impacted by stress + anxiety
        sleep_drift = -0.1 * (state["stress_level"] + state["anxiety_level"] - 10)
        state["sleep_quality"] = clamp(
            state["sleep_quality"] + sleep_drift
        )

        # Mood stability impacted by anxiety + sleep
        mood_drift = -0.12 * (state["anxiety_level"] - state["sleep_quality"])
        state["mood_stability"] = clamp(
            state["mood_stability"] + mood_drift
        )

        # Treatment adherence natural decay
        adherence_decay = random.uniform(-0.4, 0.2)
        state["treatment_adherence"] = clamp(
            state["treatment_adherence"] + adherence_decay
        )

        # Support system buffering effect
        buffer = (state["support_system"] - 5) * 0.05

        state["stress_level"] = clamp(state["stress_level"] - buffer)
        state["anxiety_level"] = clamp(state["anxiety_level"] - buffer)

        history.append(copy.deepcopy(state))

    return history
