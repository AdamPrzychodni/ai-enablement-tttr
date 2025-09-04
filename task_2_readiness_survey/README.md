# AI Readiness Assessment Tool

This project is a Streamlit web application designed to help nonprofits assess their readiness for AI transformation through a guided survey. The tool generates a personalized report with scores and actionable recommendations.

-----

## Docuemntation

This directory contains all the documentation for the project, following a logical progression from initial requirements to future recommendations.

* `01_requirements_docs.md`: Outlines the **initial project scope, requirements, and deliverables.**
* `02_research_and_literature_review.md`: A review of **academic papers and industry best practices** that inform the project's design.
* `03_software_modeling.md`: Contains **high-level system models**, including logical flow diagrams and data structures.
* `04_software_design.md`: The **detailed software design**, covering architecture, technical stack, and component functionality.
* `05_documentation.md`: A **deep-dive technical documentation** of the source code, modules, and internal logic.
* `06_recommendations.md`: **Strategic recommendations** for the future development and evolution of the project.

-----

## Environment Setup (for Optional Feature)

The core application runs without any setup. However, to enable the optional "Generate a Narrative Report" feature, which uses an LLM, you must provide an OpenAI API key.

1.  From the project root, navigate into this directory: `cd task_2_readiness_survey`
2.  Copy the example environment file:
    ```bash
    cp .env.example .env
    ```
3.  Open the new `.env` file and add your OpenAI API key.

-----

## Running the Application

From the repository's **root** directory, run the following command:

```bash
streamlit run task_2_readiness_survey/src/main.py
```

The application will open in your web browser, typically at `http://localhost:8501`.

-----

## How to Use the Tool

The AI Readiness Assessment is a user-friendly, interactive web application.

### 1\. Complete the Survey

Once you launch the application, you will be guided through a multi-page survey covering six key areas of AI readiness.

### 2\. View Your Results

After submitting, the tool automatically calculates your scores and generates a personalized report directly in the application, including:

  - An overall readiness score and level.
  - A breakdown of scores for each category.
  - Actionable recommendations for improvement.

### 3\. Generate and Download Your Report

At the bottom of the results page, you can generate a more detailed, narrative summary of your results using AI. A download button will then appear, allowing you to save a Markdown file of your personalized report.