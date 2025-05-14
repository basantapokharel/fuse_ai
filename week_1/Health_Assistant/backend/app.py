from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai_utils import get_ai_recommendation
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Allow CORS for frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, restrict this!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Mount frontend
app.mount("/static", StaticFiles(directory="../frontend"), name="static")
@app.get("/")
async def serve_index():
    return FileResponse("../frontend/index.html")

# Pydantic model for input validation
class FitnessInput(BaseModel):
    height: float
    weight: float
    activity: str

@app.post("/api/fitness")
async def fitness_endpoint(data: FitnessInput):
    recommendation = get_ai_recommendation(data.height, data.weight, data.activity)
    return {"message": recommendation}