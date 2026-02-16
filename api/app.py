from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from core.swarm_engine import run_swarm


app = FastAPI()


# ✅ VERY IMPORTANT → Allows browser calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PatientInput(BaseModel):
    mood_stability: float
    stress_level: float
    anxiety_level: float
    sleep_quality: float
    symptom_variability: float
    treatment_adherence: float
    support_system: float


@app.post("/analyze")
def analyze_patient(patient: PatientInput):

    result = run_swarm(patient.dict())

    return result
