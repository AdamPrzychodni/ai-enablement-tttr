from fastapi import FastAPI, HTTPException
from .models import AnalyzeRequest, AnalyzeResponse, RecommendRequest, RecommendResponse
from .services import get_analysis_from_llm, get_recommendation_from_llm
import uuid

# --------------------------------------------------------------------------
# 1. API Initialization
# --------------------------------------------------------------------------

app = FastAPI(
    title="AI Architect for Nonprofit Solutions",
    description="Translates nonprofit problems into actionable AI solutions.",
    version="0.1.0",
)

# --------------------------------------------------------------------------
# 2. API Endpoints
# --------------------------------------------------------------------------

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_problem(request: AnalyzeRequest):
    """
    Analyzes a nonprofit's problem statement to extract and structure the core issues.
    """
    try:
        problem_id = f"P{uuid.uuid4().hex[:4].upper()}"
        llm_response = get_analysis_from_llm(request.problem_statement)

        return AnalyzeResponse(
            problem_id=problem_id,
            description=llm_response.get("description", "No description provided."),
            clarifying_questions=llm_response.get("clarifying_questions", []),
        )
    except Exception as e:
        # Generic error handling for unexpected issues
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/recommend", response_model=RecommendResponse)
def recommend_solution(request: RecommendRequest):
    """
    Takes the structured analysis and generates a technical recommendation.
    """
    try:
        llm_response = get_recommendation_from_llm(request)
        return RecommendResponse(
            solution_summary=llm_response.get("solution_summary", "No summary provided."),
            recommended_tech_stack=llm_response.get("recommended_tech_stack", []),
            initial_steps=llm_response.get("initial_steps", []),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --------------------------------------------------------------------------
# 3. Root Endpoint
# --------------------------------------------------------------------------

@app.get("/")
def read_root():
    """
    Root endpoint for the API.
    """
    return {"message": "Welcome to the AI Architect API for Nonprofit Solutions!"}