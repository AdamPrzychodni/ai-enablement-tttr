# AI Architect: Deep Dive Documentation

This document provides a detailed look into the internal workings of the AI Architect API, including its architecture, code flow, and the role of each component.

### 1\. System Architecture

The API is designed with a clear separation of concerns. The addition of a **vector store** for Retrieval-Augmented Generation (RAG) grounds the AI's recommendations in a curated knowledge base of real-world examples.

```mermaid
graph TD
    A[User] --> B{FastAPI Server};
    B --> C[/analyze/];
    B --> D[/recommend/];
    C --> E[services.py];
    D --> E;
    E --> J["Vector Store <br> (Knowledge Base)"];
    J --> E;
    E --> F{OpenAI API};
    F --> E;
    E --> B;
    G[models.py] -- Defines data shapes --> B;
    H[prompts.py] -- Provides templates to --> E;
    I[config.py] -- Configures --> E;     
```

### 2\. Component Descriptions

The `src` directory contains the core logic of the application, broken down into the following modules:

  * **`main.py`**: This is the main entry point for the FastAPI application. It is responsible for:

      * Initializing the FastAPI app instance.
      * Defining the API endpoints (`/`, `/analyze`, and `/recommend`).
      * Handling incoming HTTP requests and returning HTTP responses.
      * Orchestrating calls to the service layer (`services.py`) to perform the core business logic.

  * **`models.py`**: This file defines the data structures for the API using Pydantic `BaseModel`. Its purpose is to:

      * Ensure that incoming request bodies match the expected JSON structure.
      * Validate the data types of incoming fields.
      * Serialize the outgoing response data into a well-defined JSON format.
      * Serve as a clear "data contract" for what the API expects and returns.

  * **`services.py`**: This is the business logic layer of the application. It is now responsible for:

      * **Initializing the RAG Vector Store**: On startup, it loads text files from the `knowledge_base`, creates vector embeddings, and builds a `faiss` index for efficient similarity searching.
      * **Performing Vector Search**: Before calling the LLM for a recommendation, it searches the vector store for relevant context.
      * Communicating with the external OpenAI API.
      * Formatting the prompts that are sent to the Large Language Model (LLM), now including the retrieved context.
      * Parsing the JSON responses received from the LLM.

  * **`prompts.py`**: This module centralizes all the prompt templates used to instruct the LLM. Keeping prompts in a separate file makes them easier to:

      * Read, manage, and update without changing the application logic.
      * Experiment with different prompt engineering strategies.

  * **`config.py`**: This file manages the application's configuration settings. It is responsible for:

      * Loading environment variables from a `.env` file, such as the `TTTR_API_KEY`.
      * Providing a centralized `settings` object that can be imported and used throughout the application.
      * Ensuring that critical configuration, like the API key, is present at startup.

### 3\. Code Flow and Logic

The API's functionality is delivered through a two-step process. The `/recommend` flow is now enhanced with the RAG step.

#### `/analyze` Endpoint Flow

The goal of this endpoint is to take a user's unstructured problem and convert it into a structured summary with clarifying questions.

```mermaid
sequenceDiagram
    participant User
    participant main.py
    participant services.py
    participant prompts.py
    participant OpenAI API

    User->>main.py: POST /analyze with {"problem_statement": "..."}
    main.py->>main.py: Generates a unique problem_id
    main.py->>services.py: Calls get_analysis_from_llm(problem_statement)
    services.py->>prompts.py: Loads ANALYZE_PROMPT
    services.py->>services.py: Formats prompt with problem_statement
    services.py->>OpenAI API: Sends formatted prompt
    OpenAI API-->>services.py: Returns JSON with {"description": "...", "clarifying_questions": [...]}
    services.py-->>main.py: Returns parsed dictionary
    main.py->>main.py: Creates AnalyzeResponse model
    main.py-->>User: Returns 200 OK with AnalyzeResponse JSON
```

1.  The user sends a `POST` request to `/analyze` with a JSON payload containing the `problem_statement`.
2.  The `analyze_problem` function in `main.py` receives the request. The request body is validated against the `AnalyzeRequest` model.
3.  A unique `problem_id` is generated using `uuid`.
4.  The function calls `get_analysis_from_llm` from `services.py`, passing the `problem_statement` string.
5.  In `services.py`, the `ANALYZE_PROMPT` from `prompts.py` is formatted with the user's problem statement.
6.  An API call is made to the OpenAI `chat.completions` endpoint with the prepared prompt.
7.  The LLM returns a JSON object, which is parsed in `services.py` and returned to `main.py`.
8.  `main.py` constructs an `AnalyzeResponse` object from the LLM's output and the generated `problem_id`.
9.  The `AnalyzeResponse` is sent back to the user as the HTTP response.

#### `/recommend` Endpoint Flow (with RAG)

This endpoint now uses the vector store to find relevant context before generating a concrete technical solution.

```mermaid
sequenceDiagram
    participant User
    participant main.py
    participant services.py
    participant Vector Store
    participant prompts.py
    participant OpenAI API

    User->>main.py: POST /recommend with AnalyzeResponse JSON
    main.py->>services.py: Calls get_recommendation_from_llm(request_data)
    
    services.py->>Vector Store: Searches for relevant documents based on problem description
    Vector Store-->>services.py: Returns relevant context
    
    services.py->>prompts.py: Loads RECOMMEND_PROMPT
    services.py->>services.py: Formats prompt with description AND retrieved context
    services.py->>OpenAI API: Sends enhanced prompt
    OpenAI API-->>services.py: Returns JSON with solution
    services.py-->>main.py: Returns parsed dictionary
    main.py->>main.py: Creates RecommendResponse model
    main.py-->>User: Returns 200 OK with RecommendResponse JSON
```

1.  The user sends a `POST` request to `/recommend` with the full JSON response they received from the `/analyze` endpoint.
2.  The `recommend_solution` function in `main.py` calls `get_recommendation_from_llm` from `services.py`.
3.  **New Step**: `services.py` encodes the problem `description` into a vector and queries the `faiss` index to find the most similar document(s) in the knowledge base.
4.  The `RECOMMEND_PROMPT` from `prompts.py` is now formatted with both the problem `description` and the **retrieved context** from the vector store.
5.  An API call is made to the OpenAI service with this enhanced, context-rich prompt.
6.  The LLM provides a technical recommendation that is now grounded in the provided real-world examples.
7.  The response is parsed and returned to the user as a `RecommendResponse` object.

-----

## Technical Decisions

The AI Architect API was built with a focus on creating a practical, scalable, and easy-to-use tool for nonprofits.

  * **API Framework**: **FastAPI** was selected for its high performance, asynchronous capabilities, and automatic generation of interactive API documentation (via Swagger UI), which simplifies testing and integration.
  * **Language Model**: The system uses the **OpenAI API**, specifically leveraging a `gpt-3.5-turbo` model for cost-effectiveness during development. The architecture is designed to be model-agnostic, allowing for an easy upgrade to a more powerful model like `gpt-4o` by simply changing an environment variable.
  * **Architecture**: A two-step (`/analyze` and `/recommend`) pipeline was implemented. This separates the task of understanding a user's problem from generating a solution, which leads to more focused and accurate results.
  * **Retrieval-Augmented Generation (RAG)**: A simple in-memory vector store was implemented using `sentence-transformers` and `faiss`. This grounds the LLM's recommendations in a curated knowledge base of successful, real-world nonprofit projects, ensuring the suggestions are contextually relevant and proven. This approach was inspired by industry best practices, such as the World Bank's ImpactAI tool.

-----

## JSON Structure Critique

The JSON structure was designed for simplicity and clarity, but there are opportunities for improvement.

### Strengths

  * **Simplicity and Clarity**: The field names (`problem_statement`, `description`, `solution_summary`) are self-explanatory and easy to understand.
  * **Logical Flow**: The structure creates a clear "data contract" where the output of the `/analyze` endpoint is the direct input for the `/recommend` endpoint. This makes the API flow predictable and easy to follow.
  * **Statelessness**: By passing the full context (`description`, `clarifying_questions`) back to the client and requiring it in the `/recommend` call, the API remains stateless. This simplifies the architecture as no server-side session storage is needed.

### Weaknesses

  * **Data Redundancy**: The client has to send back the `description` and `clarifying_questions` that the server just provided. This increases the payload size and shifts the burden of state management to the client.
  * **Lack of Context**: The `clarifying_questions` are a simple array of strings. The structure doesn't allow for providing answers to these questions, making the interaction static rather than a dynamic conversation.
  * **Limited Extensibility**: The structure is rigid. For example, the `recommended_tech_stack` is a flat list. It would be difficult to add more detail, such as cost estimates, pros/cons, or implementation difficulty for each tool, without a significant redesign.

### Alternative Design

If given complete freedom, a more robust and interactive design would be implemented. The key change would be to make the interaction stateful and more structured.

```json
// POST /problems -> Creates a new problem, returns a URL with the problem_id
{
  "problem_statement": "We struggle with volunteer engagement."
}

// GET /problems/{problem_id} -> Retrieves the current state
{
  "id": "prob_123",
  "status": "needs_clarification",
  "description": "The nonprofit struggles with volunteer engagement.",
  "clarifying_questions": [
    {
      "id": "q_001",
      "question": "What is your current process for managing volunteers?",
      "answer": null // Client would provide an answer via a PATCH request
    },
    {
      "id": "q_002",
      "question": "What is the approximate size of your volunteer base?",
      "answer": null
    }
  ]
}

// PATCH /problems/{problem_id} -> User provides answers
{
  "answers": [
    {
      "question_id": "q_001",
      "answer_text": "We use a shared spreadsheet and manual emails."
    }
  ]
}

// GET /problems/{problem_id}/recommendation -> Generates recommendation once status is 'ready'
{
    "solution_summary": "Implement a centralized volunteer management platform with automated communication.",
    "recommended_tech_stack": [
        {
            "tool": "Salesforce Nonprofit Cloud",
            "category": "CRM",
            "justification": "Provides a comprehensive, scalable solution for volunteer management.",
            "cost_tier": "Free (for up to 10 licenses)"
        },
        {
            "tool": "Twilio",
            "category": "Communication",
            "justification": "For sending automated SMS reminders and updates.",
            "cost_tier": "Pay-as-you-go"
        }
    ],
    "initial_steps": ["..."]
}
```

#### Why this design is better:

1.  **Stateful & Interactive**: It introduces a proper conversational flow. The server manages the state, and the client can provide answers to specific questions, allowing the AI to refine its understanding.
2.  **Richer Data Structure**: The `recommended_tech_stack` is now a list of objects, not strings. This allows for adding rich context like `justification` and `cost_tier`, making the recommendations far more valuable and actionable for a nonprofit.
3.  **RESTful Design**: It follows REST principles more closely, using different endpoints (`/problems`, `/recommendation`) and HTTP methods (`POST`, `GET`, `PATCH`) for different actions, which is a more standard and scalable approach for API design.