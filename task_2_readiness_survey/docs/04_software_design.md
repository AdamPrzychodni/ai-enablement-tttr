# AI Readiness Assessment Tool: Software Design

This document outlines the software design for the AI Readiness Assessment Tool, a Streamlit application designed to help nonprofits evaluate their preparedness for AI transformation.

-----

## 1. Core Concept

The AI Readiness Assessment Tool is an interactive web application that guides nonprofits through a structured survey to assess their AI readiness. The tool then processes the survey responses to generate a comprehensive report with scores and actionable recommendations, helping organizations understand their strengths and areas for improvement.

-----

## 2. System Architecture

The tool follows a straightforward, three-step process, ensuring a user-friendly experience from start to finish.

```mermaid
sequenceDiagram
    participant User
    participant "Assessment Tool (Streamlit)"

    User->>Assessment Tool (Streamlit): **Input** <br> { Completes interactive survey }

    Assessment Tool (Streamlit)->>Assessment Tool (Streamlit): **Process** <br> 1. Calculate Category Scores <br> 2. Determine Overall Readiness Level <br> 3. Generate Recommendations

    Assessment Tool (Streamlit)-->>User: **Output** <br> { Displays Readiness Report in Markdown }
````

-----

## 3\. Technical Stack

The tool will be built using a simple yet powerful technical stack, with **Streamlit** as the core framework.

  * **Web Framework**: **Streamlit** is chosen for its ability to quickly create beautiful, interactive data applications with simple Python scripts.
  * **Data Processing**: **Pandas** and **NumPy** will be used for efficient data manipulation and calculation of the assessment scores.

-----

## 4\. Survey and Scoring

The assessment is built on a hybrid model that combines academic frameworks with nonprofit-specific industry patterns.

  * **Survey Structure**: The survey is designed to be completed in under 10 minutes and is divided into 5-7 core readiness categories, such as **Digital Infrastructure**, **Leadership & Culture**, and **Data Readiness**. The questions will use a mix of Likert scales and multiple-choice formats to gather both quantitative and qualitative data.
  * **Scoring Methodology**: The tool will use a quantitative scoring engine inspired by the Analytic Hierarchy Process (AHP) to provide a nuanced and defensible readiness score. The scoring system will combine a simple 5-level maturity model with a weighted scoring system that reflects the unique priorities of each nonprofit.

-----

## 5\. Data Structures

The data structures are designed for clarity and simplicity, using Pydantic models for a clear representation of the data.

### Survey Input

The user's responses will be captured and processed in a structured format.

```python
class SurveyResponse(BaseModel):
    category: str
    question_id: str
    answer: int

class SurveyInput(BaseModel):
    organization_name: str
    responses: List[SurveyResponse]
```

### Report Output

The final report will be generated with a clear and organized structure.

```python
class CategoryResult(BaseModel):
    category_name: str
    score: int
    recommendations: List[str]

class ReadinessReport(BaseModel):
    organization_name: str
    overall_readiness_level: str
    overall_score: int
    category_results: List[CategoryResult]
```

-----

## 6\. Future Enhancements

The tool is designed with future enhancements in mind to provide even greater value to nonprofits.

  * **Ethical Framework Integration**: A dedicated module based on Responsible AI principles (fairness, transparency, accountability) could be integrated to assess ethical preparedness.
  * **Benchmarking and Peer Comparison**: A feature could be added to allow nonprofits to anonymously benchmark their readiness scores against similar organizations, providing valuable context and encouraging continuous improvement.
  * **Granular Skills Assessment**: An advanced skills module could be developed to provide a detailed analysis of a nonprofit's workforce's AI literacy and generate targeted recommendations for professional development.
  