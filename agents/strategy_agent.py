from core.llm import llm_call

class StrategyAgent:

    def evaluate(self, patient):

        prompt = f"""
        You are a Strategic Clinical Cognition Agent.

        Patient Signals:
        {patient}

        Evaluate:
        - Functional recovery potential
        - Opportunity for intervention success
        - Positive trajectory indicators
        """

        return llm_call(prompt)
