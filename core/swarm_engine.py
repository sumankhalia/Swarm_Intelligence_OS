from core.scoring_models import *
from core.llm import LLMBrain

brain = LLMBrain()


def agent_reasoning(role, patient, scores):

    prompt = f"""
    You are acting as the {role} Agent in a Swarm Cognitive Intelligence System.

    Patient Signals:
    {patient}

    Cognitive Scores:
    {scores}

    Provide:
    - Key Observations
    - Interpretation
    - Strategic Concern
    """

    return brain.analyze_text(prompt)


def run_swarm(patient):

    strategy = strategy_score(patient)
    risk = risk_score(patient)
    governance = governance_score(patient)
    skeptic = skeptic_pressure(strategy, risk)

    scores = {
        "Strategy": round(strategy, 2),
        "Risk": round(risk, 2),
        "Governance": round(governance, 2),
        "SkepticPressure": round(skeptic, 2),
    }

    composite = composite_score(strategy, risk, governance, skeptic)

    decision = executive_decision(composite)

    # 🔥 Individual Agent Cognition
    strategy_agent = agent_reasoning("Strategy", patient, scores)
    risk_agent = agent_reasoning("Risk", patient, scores)
    skeptic_agent = agent_reasoning("Skeptic", patient, scores)
    governance_agent = agent_reasoning("Governance", patient, scores)

    # 🔥 Final Executive Reasoning
    final_reasoning = brain.analyze(patient, scores, decision)

    return {
        "decision": decision,
        "confidence": confidence_score(composite),
        "scores": scores,
        "strategy_agent": strategy_agent,
        "risk_agent": risk_agent,
        "skeptic_agent": skeptic_agent,
        "governance_agent": governance_agent,
        "reasoning": final_reasoning,
    }
