from core.swarm_engine import run_swarm
from data.synthetic_data import generate_patient

print("\nInitializing Swarm Cognitive Intelligence System...\n")

patient = generate_patient()

print("Synthetic Patient Data:\n")

for k, v in patient.items():
    print(f"{k}: {v}")

print("\nRunning Swarm Intelligence Analysis...\n")

result = run_swarm(patient)

print("\nFINAL EXECUTIVE DECISION:\n")
print(result["decision"])
print("Confidence:", result["confidence"], "%")

print("\nCognitive Scores:\n", result["scores"])

print("\n--- Strategy Agent ---\n")
print(result["strategy_agent"])

print("\n--- Risk Agent ---\n")
print(result["risk_agent"])

print("\n--- Skeptic Agent ---\n")
print(result["skeptic_agent"])

print("\n--- Governance Agent ---\n")
print(result["governance_agent"])

print("\n--- Executive Cognitive Reasoning ---\n")
print(result["reasoning"])
