import json
from openai import OpenAI
from config import settings

# Initialize the OpenAI client with the API key from settings
client = OpenAI(api_key=settings.TTTR_API_KEY)

def generate_llm_report(overall_score, readiness_level, readiness_description, category_scores, recommendations):
    """
    Generates a human-readable report using an LLM.

    Args:
        overall_score (int): The overall readiness score.
        readiness_level (str): The calculated readiness level (e.g., "Emerging").
        readiness_description (str): A brief description of the readiness level.
        category_scores (dict): A dictionary of scores for each category.
        recommendations (dict): A dictionary of recommendations for each category.

    Returns:
        str: A markdown-formatted, human-readable report.
    """
    prompt = f"""
    You are an expert AI strategist for nonprofit organizations. Your task is to write a human-readable, encouraging, and actionable
    AI Readiness Report based on the provided data. The report should be in Markdown format.

    **Report Data:**
    - **Overall Score:** {overall_score}/100
    - **Readiness Level:** {readiness_level} ({readiness_description})
    - **Category Scores:** {json.dumps(category_scores, indent=2)}
    - **Recommendations:** {json.dumps(recommendations, indent=2)}

    **Instructions:**
    1.  **Start with a positive and encouraging tone.** Acknowledge the effort the organization has put into thinking about its future.
    2.  **Write a brief Executive Summary.** Explain the overall score and readiness level in simple terms.
    3.  **For each category, provide a narrative analysis.** Explain what the score means in practical terms.
    4.  **Integrate the specific recommendations naturally into the analysis for each category.** Frame them as actionable next steps.
    5.  **Conclude with a summary of the top 3 priority actions** and a motivational closing statement.
    6.  **Use Markdown for formatting** (e.g., headers, bold text, bullet points).
    """

    try:
        response = client.chat.completions.create(
            model=settings.TTTR_MODEL,
            messages=[{"role": "system", "content": prompt}],
            temperature=settings.TTTR_TEMPERATURE,
        )
        report_content = response.choices[0].message.content
        return report_content if report_content else "Error: Could not generate the report."
    except Exception as e:
        print(f"An error occurred while generating the LLM report: {e}")
        return "An error occurred while generating the report. Please check the logs."