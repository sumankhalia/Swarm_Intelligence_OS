from core.llm import llm_call

class SkepticAgent:

    def evaluate(self, patient):

        prompt = f"""
        You are a Skeptical Diagnostic Agent.

        Patient Signals:
        {patient}

        Challenge:
        - Hidden contradictions
        - Over-optimistic interpretations
        - Missing information risks
        """

        return llm_call(prompt)
