## Software Model: AI Architect API (Demo Version)

### 1. Core Concept

This model represents an API designed to translate a nonprofit's problem into an actionable AI-driven solution. It functions as a simple, two-step conversation:

1.  **Analyze**: Understand the user's problem.
2.  **Recommend**: Propose a solution.

### 2. System Behavior (Logical Flow)

The system's behavior is a clear sequence: the user first gets their problem analyzed, and then uses that analysis to get a recommendation.

```mermaid
sequenceDiagram
    participant User
    participant API

    User->>API: **POST /analyze** <br> { "problem_statement": "We need help managing volunteers." }

    API-->>User: **Response** <br> { "problem_id": "P01", "description": "Need a system to manage volunteers.", "clarifying_questions": [...] }

    User->>API: **POST /recommend** <br> { "problem_id": "P01", "description": "...", "clarifying_questions": [] }

    API-->>User: **Response** <br> { "solution_summary": "...", "recommended_tech_stack": [...], "initial_steps": [...] }
````

### 3\. Data Structure (The "Language" of the API)

These are the simple data structures the API speaks. Using Pydantic models provides a clear and abstract representation.

#### **Input & Output for `/analyze`**

```python
# User sends this:
class AnalyzeRequest(BaseModel):
    problem_statement: str

# User receives this:
class AnalyzeResponse(BaseModel):
    problem_id: str
    description: str
    clarifying_questions: List[str]
```

#### **Input & Output for `/recommend`**

```python
# User sends the output from /analyze:
class RecommendRequest(BaseModel):
    problem_id: str
    description: str
    clarifying_questions: List[str]

# User receives this:
class RecommendResponse(BaseModel):
    solution_summary: str
    recommended_tech_stack: List[str]
    initial_steps: List[str]
```

### 4\. Functionality (Endpoint Definitions)

This is a simplified view of what each part of the API does.

#### `POST /analyze`

  * **Purpose**: To structure a vague problem.
  * **Input**: A simple JSON object with a `problem_statement`.
  * **Output**: A structured JSON object containing a summary and questions.

#### `POST /recommend`

  * **Purpose**: To generate a solution from a structured problem.
  * **Input**: The exact JSON output from the `/analyze` endpoint.
  * **Output**: A JSON object with a summary, tech stack, and actionable first steps.
