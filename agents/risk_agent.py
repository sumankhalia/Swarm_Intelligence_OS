from core.llm import llm_call

class RiskAgent:

    def evaluate(self, patient):

        prompt = f"""
        You are a Clinical Risk Intelligence Agent.

        Patient Signals:
        {patient}

        Evaluate:
        - Psychological deterioration risk
        - Instability threats
        - Red flag detection
        """

        return llm_call(prompt)
