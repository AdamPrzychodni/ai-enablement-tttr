import json
from openai import OpenAI
from .config import settings
from .prompts import ANALYZE_PROMPT, RECOMMEND_PROMPT
from .models import RecommendRequest

# Initialize the OpenAI client
client = OpenAI(api_key=settings.TTTR_API_KEY)

def get_analysis_from_llm(problem_statement: str) -> dict:
    """
    Calls the LLM to analyze the problem statement and returns a structured response.
    """
    prompt = ANALYZE_PROMPT.format(problem_statement=problem_statement)
    
    response = client.chat.completions.create(
        model=settings.TTTR_MODEL,
        messages=[{"role": "system", "content": prompt}],
        temperature=settings.TTTR_TEMPERATURE,
        response_format={"type": "json_object"},
    )
    
    # Check if the response content exists before parsing
    llm_output = response.choices[0].message.content
    if llm_output:
        try:
            return json.loads(llm_output)
        except (json.JSONDecodeError, IndexError) as e:
            print(f"Error parsing LLM response for analysis: {e}")
    
    # Fallback if content is None or parsing fails
    return {"description": "Error analyzing problem.", "clarifying_questions": []}


def get_recommendation_from_llm(analysis: RecommendRequest) -> dict:
    """
    Calls the LLM to generate a recommendation based on the structured problem.
    """
    prompt = RECOMMEND_PROMPT.format(description=analysis.description)
    
    response = client.chat.completions.create(
        model=settings.TTTR_MODEL,
        messages=[{"role": "system", "content": prompt}],
        temperature=settings.TTTR_TEMPERATURE,
        response_format={"type": "json_object"},
    )
    
    # Check if the response content exists before parsing
    llm_output = response.choices[0].message.content
    if llm_output:
        try:
            return json.loads(llm_output)
        except (json.JSONDecodeError, IndexError) as e:
            print(f"Error parsing LLM response for recommendation: {e}")
            
    # Fallback if content is None or parsing fails
    return {
        "solution_summary": "Error generating recommendation.",
        "recommended_tech_stack": [],
        "initial_steps": [],
    }
