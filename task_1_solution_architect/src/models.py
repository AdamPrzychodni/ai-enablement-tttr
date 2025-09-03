from pydantic import BaseModel
from typing import List

# /analyze endpoint
class AnalyzeRequest(BaseModel):
    problem_statement: str

class AnalyzeResponse(BaseModel):
    problem_id: str
    description: str
    clarifying_questions: List[str]

# /recommend endpoint
class RecommendRequest(BaseModel):
    problem_id: str
    description: str
    clarifying_questions: List[str]

class RecommendResponse(BaseModel):
    solution_summary: str
    recommended_tech_stack: List[str]
    initial_steps: List[str]
    