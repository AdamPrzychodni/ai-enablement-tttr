# Define weights for each category. These can be adjusted based on strategic priorities.
CATEGORY_WEIGHTS = {
    "Digital Infrastructure": 0.20,
    "Leadership & Culture": 0.20,
    "Staff Capacity": 0.15,
    "Data Readiness": 0.25,
    "Financial Resources": 0.10,
    "Use Case Clarity": 0.10,
}

def calculate_category_scores(responses, questions):
    """Calculates the score for each category based on user responses."""
    category_scores = {}
    for category, cat_questions in questions.items():
        total_possible_score = len(cat_questions) * 4  # Max score is 4 for each question
        actual_score = 0
        for q in cat_questions:
            question_key = f"{category} - {q['question']}"
            if question_key in responses:
                # Find the numeric score from the selected option string
                selected_option = responses[question_key]
                for score, text in q['options'].items():
                    if text == selected_option:
                        actual_score += score
                        break
        
        # Normalize the score to be out of 100
        category_scores[category] = (actual_score / total_possible_score) * 100
    return category_scores

def calculate_overall_score(category_scores):
    """Calculates the weighted overall readiness score."""
    overall_score = 0
    for category, score in category_scores.items():
        overall_score += score * CATEGORY_WEIGHTS.get(category, 0)
    return int(overall_score)

def get_readiness_level(overall_score):
    """Determines the readiness level based on the overall score."""
    if overall_score <= 25:
        return "Foundational", "Needs to build basic digital infrastructure before considering AI."
    elif 26 <= overall_score <= 50:
        return "Emerging", "In the early stages of building AI capabilities."
    elif 51 <= overall_score <= 75:
        return "Ready", "Well-prepared for AI adoption with a solid foundation."
    else:
        return "Advanced", "Optimized for AI transformation and ready to leverage AI for significant impact."
