def route_task(patient):

    volatility = patient["symptom_variability"]
    anxiety = patient["anxiety_level"]
    stability = patient["mood_stability"]

    routing_map = []

    if anxiety > 6:
        routing_map.append("risk")

    if volatility > 5:
        routing_map.append("skeptic")

    if stability > 4:
        routing_map.append("strategy")

    routing_map.append("governance")  # Always needed

    return routing_map
