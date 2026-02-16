import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load local .env (harmless on Render)
load_dotenv()

# ✅ Works BOTH locally + Render
api_key = (
    os.getenv("GOOGLE_API_KEY")     # Render / Production
    or os.getenv("GEMINI_API_KEY")  # Local / Development
)

if not api_key:
    raise ValueError("Missing API Key (GOOGLE_API_KEY or GEMINI_API_KEY)")

genai.configure(api_key=api_key)


class LLMBrain:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    # ✅ Executive reasoning
    def analyze(self, patient, scores, decision):

        prompt = f"""
You are the Executive Cognitive AI of a Swarm Intelligence System.

Patient Signals:
{patient}

Cognitive Scores:
{scores}

Executive Decision:
{decision}

Provide professional clinical reasoning explaining:

• Emotional interpretation
• Dominant psychological pressures
• Contradictions / patterns
• High-level executive insight
"""

        try:
            response = self.model.generate_content(prompt)
            return response.text

        except Exception as e:
            return f"LLM temporarily unavailable: {str(e)}"

    # ✅ Agent-level reasoning
    def analyze_text(self, prompt):

        try:
            response = self.model.generate_content(prompt)
            return response.text

        except Exception as e:
            return f"Agent reasoning unavailable: {str(e)}"
