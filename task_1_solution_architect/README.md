# AI Architect for Nonprofit Solutions

This project is a FastAPI server that acts as an "AI Architect." It's designed to help nonprofits translate vague problem statements into actionable, AI-driven technical solutions.

The API exposes two main endpoints:
-   `/analyze`: Takes a free-form problem statement and structures it, identifying the core issue and asking clarifying questions.
-   `/recommend`: Takes the structured problem and suggests a technical solution, including a tech stack and initial steps.

---

## Setup and Installation

1.  **Navigate to the project directory:**
    ```bash
    cd path/to/your/ai-enablement-tttr
    ```

2.  **Create and populate your environment file:**
    Copy the example environment file.
    ```bash
    cp task_1_solution_architect/.env.example task_1_solution_architect/.env
    ```
    Then, open `task_1_solution_architect/.env` and add your OpenAI API key.

3.  **Install dependencies:**
    Ensure you have a virtual environment activated and then run:
    ```bash
    pip install -r requirements.txt
    ```

---

## Running the Server

To run the FastAPI server, navigate to the `task_1_solution_architect` directory and use `uvicorn`:

```bash
cd task_1_solution_architect
uvicorn src.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

---

## API Usage (cURL Examples)

Here is a complete example of how to interact with the API from a new terminal.

### 1. Call the `/analyze` Endpoint

Send the nonprofit's problem statement.

**Request:**

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
-H "Content-Type: application/json" \
-d '{
  "problem_statement": "We are a small environmental nonprofit and we struggle to keep our donors engaged. Our email open rates are low and we do not have a clear way to track interactions."
}'
```

**Response:**

Note: The response you receive will be different from this example. The problem_id is dynamically generated for each request, and the AI-generated description and clarifying_questions will also vary slightly. This is expected behavior.

```json
{
  "problem_id": "P2944",
  "description": "The nonprofit faces challenges in engaging donors due to low email open rates and lack of interaction tracking.",
  "clarifying_questions": [
    "What email marketing tools or platforms are currently being used?",
    "Are there specific types of content or campaigns that have shown better engagement?",
    "What resources are available for implementing a donor engagement tracking system?"
  ]
}
```

### 2. Call the `/recommend` Endpoint

Use the full JSON object from the `/analyze` response to get a recommendation. Note how we've included answers to the clarifying questions to get a better recommendation.

**Request:**

```bash
curl -X POST "http://127.0.0.1:8000/recommend" \
-H "Content-Type: application/json" \
-d '{
  "problem_id": "P2944",
  "description": "The nonprofit faces challenges in engaging donors due to low email open rates and lack of interaction tracking.",
  "clarifying_questions": [
    "What email marketing tools or platforms are currently being used? (Answer: We use Mailchimp sporadically)",
    "Are there specific types of content or campaigns that have shown better engagement? (Answer: Newsletters with success stories get slightly better opens)",
    "What resources are available for implementing a donor engagement tracking system? (Answer: Very limited budget, one part-time person for marketing)"
  ]
}'
```

**Response:**

```json
{
  "solution_summary": "Implement an email marketing automation system to increase donor engagement and track interactions effectively.",
  "recommended_tech_stack": [
    "Set up automated email campaigns for donation reminders, impact updates, and success stories to increase engagement.",
    "Integrate Google Analytics to track email open rates, click-through rates, and donor interactions for data-driven decision-making."
  ]
}
```

