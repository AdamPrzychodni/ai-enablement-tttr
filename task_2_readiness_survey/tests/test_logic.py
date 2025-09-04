import pytest
import sys
import os

# Add the project root directory to the Python path
# This allows us to import from the 'src' module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.scoring import calculate_category_scores, calculate_overall_score, get_readiness_level
from src.recommendations import get_recommendations
from src.survey_questions import SURVEY_QUESTIONS

# --- Test Data ---
# Represents a sample "AI Ready" organization's responses
SAMPLE_RESPONSES_READY = {
    "Digital Infrastructure - Which of these best describes the tools and systems your organization currently relies on?": "We use a well-integrated set of modern tools (e.g., CRM, project management software).",
    "Digital Infrastructure - How would you describe the way your organization manages data today?": "We rely on a well-maintained central system (e.g., CRM, data warehouse).",
    "Leadership & Culture - How does your leadership team currently view technology and AI?": "They are supportive and encourage us to explore AI when possible.",
    "Leadership & Culture - Which of these feels closest to your organization’s attitude toward trying new approaches?": "We are generally open to experimenting with new ideas and tools.",
    "Staff Capacity - How would you describe your team’s comfort level with technology?": "We have a healthy mix of digital skills, including some data analysis expertise.",
    "Staff Capacity - What opportunities do staff have to grow their technical skills?": "We provide access to online learning and encourage professional development.",
    "Data Readiness - How would you describe the quality and completeness of your organization’s data?": "Our data is generally reliable, well-structured, and usable.",
    "Data Readiness - Does your organization have clear practices for managing and protecting data?": "Yes, we have a policy that covers data privacy and security.",
    "Financial Resources - How is technology currently funded in your organization?": "We have a dedicated technology budget and are open to AI investments.",
    "Financial Resources - How does your organization think about the value of technology investments?": "We evaluate expected ROI before making technology decisions.",
    "Use Case Clarity - How clear is your organization about where AI could be most helpful?": "We’ve identified one or two clear, specific problems that AI could help solve.",
    "Use Case Clarity - Has your organization defined how it would measure success for AI projects?": "Yes, we have clear, measurable KPIs for at least one priority use case."
}

def test_calculate_category_scores():
    """
    Tests that category scores are calculated correctly based on sample responses.
    """
    # For this sample data, every answer is the 3rd option, which has a score of 3.
    # Total possible score per category is 2 questions * 4 max points = 8.
    # Actual score is 2 questions * 3 points = 6.
    # Expected normalized score = (6 / 8) * 100 = 75.
    expected_scores = {
        "Digital Infrastructure": 75.0,
        "Leadership & Culture": 75.0,
        "Staff Capacity": 75.0,
        "Data Readiness": 75.0,
        "Financial Resources": 75.0,
        "Use Case Clarity": 75.0,
    }
    
    calculated_scores = calculate_category_scores(SAMPLE_RESPONSES_READY, SURVEY_QUESTIONS)
    assert calculated_scores == expected_scores

def test_calculate_overall_score():
    """
    Tests that the weighted overall score is calculated correctly.
    """
    category_scores = {
        "Digital Infrastructure": 75, "Leadership & Culture": 75,
        "Staff Capacity": 75, "Data Readiness": 75,
        "Financial Resources": 75, "Use Case Clarity": 75,
    }
    # Since all category scores are 75, the weighted average must also be 75.
    overall_score = calculate_overall_score(category_scores)
    assert overall_score == 75

def test_get_readiness_levels():
    """
    Tests the readiness level mapping for different score thresholds.
    """
    assert get_readiness_level(20)[0] == "Foundational"
    assert get_readiness_level(40)[0] == "Emerging"
    assert get_readiness_level(60)[0] == "Ready"
    assert get_readiness_level(90)[0] == "Advanced"

def test_get_recommendations():
    """
    Tests that the recommendation engine returns the correct advice for different scores.
    """
    # Test for low scores (<= 50)
    low_scores = {"Digital Infrastructure": 40, "Leadership & Culture": 40}
    low_recs = get_recommendations(low_scores)
    assert "Focus on centralizing data storage" in low_recs["Digital Infrastructure"][0]
    assert "Share success stories" in low_recs["Leadership & Culture"][0]
    
    # Test for high scores (> 50)
    high_scores = {"Digital Infrastructure": 80, "Leadership & Culture": 80}
    high_recs = get_recommendations(high_scores)
    assert "Investigate cloud services" in high_recs["Digital Infrastructure"][0]
    assert "Develop a formal AI strategy" in high_recs["Leadership & Culture"][0]
    