import os
from openai import OpenAI


# ✅ Production-safe client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


class LLMBrain:

    def analyze(self, patient, scores, decision):

        prompt = f"""
You are the Executive Cognitive AI of a Swarm Intelligence System.

Patient Signals:
{patient}

Cognitive Scores:
{scores}

Executive Decision:
{decision}

Provide professional clinical reasoning explaining the psychological interpretation,
dominant pressures, contradictions, and executive assessment.
"""

        try:
            response = client.chat.completions.create(
                model="gpt-4.1-nano",
                messages=[
                    {"role": "user", "content": prompt}
                ],
            )

            return response.choices[0].message.content

        except Exception as e:
            print("LLM Failure:", str(e))
            return "Cognitive reasoning temporarily unavailable."


    def analyze_text(self, prompt):

        try:
            response = client.chat.completions.create(
                model="gpt-4.1-nano",
                messages=[
                    {"role": "user", "content": prompt}
                ],
            )

            return response.choices[0].message.content

        except Exception as e:
            print("LLM Failure:", str(e))
            return "Agent reasoning temporarily unavailable."
