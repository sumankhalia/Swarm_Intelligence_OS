import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Missing GEMINI_API_KEY in .env")

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

        response = self.model.generate_content(prompt)
        return response.text

    def analyze_text(self, prompt):

        response = self.model.generate_content(prompt)
        return response.text
