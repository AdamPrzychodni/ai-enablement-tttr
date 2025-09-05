# AI Architect for Nonprofit Solutions

This project is a FastAPI server that acts as an "AI Architect." It's designed to help nonprofits translate vague problem statements into actionable, AI-driven technical solutions via a two-step API process.

The API exposes two main endpoints:

  - `/analyze`: Takes a free-form problem statement and structures it.
  - `/recommend`: Takes the structured problem and suggests a technical solution.

-----

## Documentation

This directory contains all the documentation for the project, following a logical progression from initial requirements to future recommendations.

* `01_requirements_docs.md`: Outlines the **initial project scope, requirements, and deliverables.**
* `02_research_and_literature_review.md`: A review of **academic papers and industry best practices** that inform the project's design.
* `03_software_modeling.md`: Contains **high-level system models**, including logical flow diagrams and data structures.
* `04_software_design.md`: The **detailed software design**, covering architecture, technical stack, and component functionality.
* `05_documentation.md`: A **deep-dive technical documentation** of the source code, modules, and internal logic.
* `06_recommendations.md`: **Strategic recommendations** for the future development and evolution of the project.
* `07_demo_cases.md`: **Concrete examples** of the end-to-end API workflow, from problem statement to final recommendation.

-----

## Environment Setup

Before running the server, you need to provide your OpenAI API key.

1.  From the project root, navigate into this directory: 
    ```bash
    cd task_1_solution_architect  
    ```
2.  Copy the example environment file:
    ```bash
    cp .env.example .env
    ```
3.  Open the new `.env` file and add your OpenAI API key.
4.  Go back to **root** directory.
    ```bash
    cd ..
    ```

-----

## Running the Server

From the repository's **root** directory, run the following command:

```bash
uvicorn task_1_solution_architect.src.main:app --reload
````

The API will be available at `http://127.0.0.1:8000`.

-----

## API Usage (cURL Examples)

Here is a complete example of how to interact with the API.

### 1\. Call the `/analyze` Endpoint

Send a problem statement to structure it.

**Request:**

```bash
curl -X POST "[http://127.0.0.1:8000/analyze](http://127.0.0.1:8000/analyze)" \
-H "Content-Type: application/json" \
-d '{
  "problem_statement": "We are a small environmental nonprofit and we struggle to keep our donors engaged. Our email open rates are low and we do not have a clear way to track interactions."
}'
```

**Response:**

```json
{
  "problem_id": "P2944",
  "description": "The nonprofit faces challenges in engaging donors due to low email open rates and lack of interaction tracking.",
  "clarifying_questions": [
    "What email marketing tools or platforms are currently being used?",
    "What resources are available for implementing a donor engagement tracking system?"
  ]
}
```

### 2\. Call the `/recommend` Endpoint

Use the full JSON object from the `/analyze` response to get a recommendation.

**Request:**

```bash
curl -X POST "[http://127.0.0.1:8000/recommend](http://127.0.0.1:8000/recommend)" \
-H "Content-Type: application/json" \
-d '{
  "problem_id": "P2944",
  "description": "The nonprofit faces challenges in engaging donors due to low email open rates and lack of interaction tracking.",
  "clarifying_questions": []
}'
```

**Response:**

```json
{
  "solution_summary": "Implement an email marketing automation system to increase donor engagement...",
  "recommended_tech_stack": ["Mailchimp or SendGrid for automated email campaigns...", "Google Analytics for tracking..."],
  "initial_steps": ["Segment your donor list...", "Set up a welcome email series..."]
}
```

### 3\. End-to-End Test (One-Liner Command)

For efficient testing, you can chain the `/analyze` and `/recommend` calls into a single command. This pipes the output of the first request directly as the input for the second.

**Example with Pretty-Printing (using `jq`):**

This example uses the HelpMum problem statement and formats the final JSON output for readability.

```bash
curl -s -X POST "[http://127.0.0.1:8000/analyze](http://127.0.0.1:8000/analyze)" \
-H "Content-Type: application/json" \
-d '{
  "problem_statement": "Our healthcare workers in Nigeria lack the tools to quickly identify high-risk pregnancies. We need an AI-powered system that helps them stratify risk levels early in antenatal care, so they can provide the right tailored support for each mother and prevent complications."
}' | curl -s -X POST "[http://127.0.0.1:8000/recommend](http://127.0.0.1:8000/recommend)" \
-H "Content-Type: application/json" \
-d @- | jq '.'
```

**Response:**

```json
{
  "solution_summary": "Develop an AI-powered platform similar to Jacaranda Health's PROMPTS to assist healthcare workers in identifying high-risk pregnancies quickly.",
  "recommended_tech_stack": [
    "Messaging Gateway: Utilize a regional SMS gateway like Africa's Talking for reliable and cost-effective communication.",
    "Backend: Implement Python with Django or FastAPI for managing the platform's logic and data.",
    "AI/NLP: Use standard libraries like spaCy for entity recognition and Scikit-learn for text classification models.",
    "Database: Employ a robust open-source database like PostgreSQL for securely handling patient data.",
    "Dashboard: Utilize an open-source tool like Metabase for healthcare workers to view flagged cases and patient history."
  ],
  "initial_steps": [
    "Conduct a needs assessment to understand the specific requirements of healthcare workers in Nigeria for identifying high-risk pregnancies.",
    "Develop a prototype of the AI-powered platform with basic features to demonstrate its functionality and potential impact.",
    "Pilot the platform with a small group of healthcare workers to gather feedback and iterate on the design based on their input.",
    "Train healthcare workers on how to use the platform effectively and integrate it into their existing workflow.",
    "Monitor the platform's performance and gather data on its effectiveness in identifying high-risk pregnancies for continuous improvement."
  ]
}
```