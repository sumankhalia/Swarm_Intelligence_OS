import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# ✅ Proper key resolution (Production First)
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Missing API Key (GOOGLE_API_KEY or GEMINI_API_KEY)")

genai.configure(api_key=api_key)


class LLMBrain:

    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def analyze(self, patient, scores, decision):

        prompt = f"""
You are the Executive Cognitive AI of a Swarm Intelligence System.

Patient Signals:
{patient}

Cognitive Scores:
{scores}

Executive Decision:
{decision}

Provide professional clinical reasoning.
"""

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print("LLM Failure:", str(e))
            return "LLM unavailable – Cognitive fallback activated."

    def analyze_text(self, prompt):

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print("LLM Failure:", str(e))
            return "LLM unavailable – Cognitive fallback activated."
