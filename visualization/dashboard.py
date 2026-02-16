import matplotlib.pyplot as plt
import numpy as np

def plot_population_trends(history):

    stress_levels = []

    for month_data in history:
        avg_stress = np.mean([p["stress_level"] for p in month_data])
        stress_levels.append(avg_stress)

    plt.figure()
    plt.plot(stress_levels)
    plt.title("Population Stress Evolution")
    plt.xlabel("Months")
    plt.ylabel("Average Stress")
    plt.show()
