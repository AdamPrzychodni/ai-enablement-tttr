import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
import sys
import os

# Add the project root directory to the Python path
# This allows us to import from the 'src' module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import app

client = TestClient(app)

@patch("src.main.get_analysis_from_llm")
def test_analyze_problem_success(mock_get_analysis):
    """
    Tests the /analyze endpoint for a successful response.
    """
    # Configure the mock to return a successful response
    mock_get_analysis.return_value = {
        "description": "A test description of the problem.",
        "clarifying_questions": ["What is the primary goal?"],
    }

    response = client.post("/analyze", json={"problem_statement": "This is a test problem."})
    
    # Assert that the request was successful
    assert response.status_code == 200
    
    # Assert that the response body contains the expected keys and data types
    data = response.json()
    assert "problem_id" in data
    assert isinstance(data["problem_id"], str)
    assert data["description"] == "A test description of the problem."
    assert data["clarifying_questions"] == ["What is the primary goal?"]

@patch("src.main.get_recommendation_from_llm")
def test_recommend_solution_success(mock_get_recommendation):
    """
    Tests the /recommend endpoint for a successful response.
    """
    # Configure the mock to return a successful recommendation
    mock_get_recommendation.return_value = {
        "solution_summary": "Implement a test solution.",
        "recommended_tech_stack": ["pytest", "fastapi"],
        "initial_steps": ["Write a test", "Run the test"],
    }

    # This is the expected input for the /recommend endpoint
    request_data = {
        "problem_id": "P1234",
        "description": "A test description.",
        "clarifying_questions": [],
    }
    
    response = client.post("/recommend", json=request_data)
    
    # Assert that the request was successful
    assert response.status_code == 200
    
    # Assert that the response body contains the expected data
    data = response.json()
    assert data["solution_summary"] == "Implement a test solution."
    assert data["recommended_tech_stack"] == ["pytest", "fastapi"]
    assert data["initial_steps"] == ["Write a test", "Run the test"]

def test_read_root():
    """
    Tests the root endpoint to ensure it's active.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the AI Architect API for Nonprofit Solutions!"}

@patch("src.main.get_analysis_from_llm")
def test_analyze_problem_llm_error(mock_get_analysis):
    """
    Tests the /analyze endpoint's error handling when the LLM call fails.
    """
    # Configure the mock to simulate an exception
    mock_get_analysis.side_effect = Exception("LLM is down")

    response = client.post("/analyze", json={"problem_statement": "This will fail."})
    
    # Assert that the server returns a 500 Internal Server Error
    assert response.status_code == 500
    assert response.json() == {"detail": "LLM is down"}
    