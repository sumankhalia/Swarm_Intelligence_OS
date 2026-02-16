import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("⚠ No API Key found → Running in Cognitive Simulation Mode")
else:
    genai.configure(api_key=api_key)


class LLMBrain:
    def __init__(self):
        try:
            self.model = genai.GenerativeModel("gemini-2.5-flash")
            self.available = True
        except:
            self.available = False

    def safe_generate(self, prompt):

        if not self.available:
            return "LLM unavailable – Running deterministic cognitive reasoning."

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print("LLM Failure:", str(e))
            return "LLM temporarily unavailable – Cognitive engine fallback activated."

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

        return self.safe_generate(prompt)

    def analyze_text(self, prompt):
        return self.safe_generate(prompt)
