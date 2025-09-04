# AI Architect for Nonprofit Solutions

This project is a FastAPI server that acts as an "AI Architect." It's designed to help nonprofits translate vague problem statements into actionable, AI-driven technical solutions via a two-step API process.

The API exposes two main endpoints:

  - `/analyze`: Takes a free-form problem statement and structures it.
  - `/recommend`: Takes the structured problem and suggests a technical solution.

-----

## Environment Setup

Before running the server, you need to provide your OpenAI API key.

1.  From the project root, navigate into this directory: `cd task_1_solution_architect`
2.  Copy the example environment file:
    ```bash
    cp .env.example .env
    ```
3.  Open the new `.env` file and add your OpenAI API key.

-----

## Running the Server

From the repository's **root** directory, run the following command:

```bash
uvicorn task_1_solution_architect.src.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

-----

## API Usage (cURL Examples)

Here is a complete example of how to interact with the API.

### 1\. Call the `/analyze` Endpoint

Send a problem statement to structure it.

**Request:**

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
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
curl -X POST "http://127.0.0.1:8000/recommend" \
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