# AI Readiness Assessment Tool

This project is a Streamlit web application that is AI Assesment Survey for organizations. It's designed to help nonprofits assess their readiness for AI transformation through a guided survey.

The tool walks a user through a series of questions covering key readiness areas and then generates a personalized report with scores and actionable recommendations. An optional feature allows for generating a more detailed narrative report using an LLM.

-----

## Setup and Installation

1.  **Navigate to the project directory:**

    ```bash
    cd path/to/your/ai-enablement-tttr
    ```

2.  **Create and populate your environment file:**
    Copy the example environment file. This step is necessary for the optional narrative report generation feature.

    ```bash
    cp task_2_readiness_survey/.env.example task_2_readiness_survey/.env
    ```

    Then, open `task_2_readiness_survey/.env` and add your OpenAI API key.

3.  **Install dependencies:**
    Ensure you have a virtual environment activated and then run:

    ```bash
    pip install -r requirements.txt
    ```

-----

## Running the Application

To run the Streamlit application, navigate to the project's root directory and use the `streamlit run` command:

```bash
streamlit run task_2_readiness_survey/src/main.py
```

The application will be available in your web browser, typically at `http://localhost:8501`.

-----

## How to Use the Tool

The AI Readiness Assessment is an interactive web application.

### 1\. Complete the Survey

Once you launch the application, you will be guided through a multi-page survey. The questions cover six key areas of AI readiness, from your digital infrastructure to your team's capacity.

### 2\. View Your Results

After submitting the survey, the tool will automatically calculate your scores and generate a personalized report directly in the application. This report includes:

  - An overall readiness score and level.
  - A breakdown of scores for each category.
  - Actionable recommendations for areas of improvement.

### 3\. Generate and Download Your Report

At the bottom of the results page, you have the option to generate a more detailed, narrative summary of your results. After generating the report, a download button will appear, allowing you to save a Markdown file of your personalized report.