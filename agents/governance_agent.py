from core.llm import llm_call

class GovernanceAgent:

    def evaluate(self, patient):

        prompt = f"""
        You are a Clinical Governance Agent.

        Patient Signals:
        {patient}

        Evaluate:
        - Ethical intervention boundaries
        - Sustainability of treatment
        - Compliance & safety logic
        """

        return llm_call(prompt)
