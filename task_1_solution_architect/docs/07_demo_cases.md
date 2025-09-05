# API Demo Cases

This document provides concrete examples of the end-to-end workflow for the AI Architect API. Each case demonstrates how the API translates a real-world nonprofit challenge into an actionable technical recommendation, grounded in an inspirational project from our curated knowledge base.

-----

## Demo Case 1: Savana Signatures, Ghana

  - **Project Link**: [https://app.techtotherescue.org/project-brief/recTLXFImjilnKyz4](https://app.techtotherescue.org/project-brief/recTLXFImjilnKyz4)
  - **Knowledge Base Inspiration**: Jacaranda Health's AI-Powered Maternal Health Platform (Kenya)

### 1\. Analyze Request

The process begins with a concise, human-centered problem statement.

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
-H "Content-Type: application/json" \
-d '{
  "problem_statement": "In Northern Ghana, we''re fighting to prevent the tragic deaths of mothers and babies, but our mobile health platforms can''t keep up. We need a smarter system that can do three critical things: analyze our data to predict high-risk pregnancies before it''s too late, communicate with mothers in their own local languages instead of just English, and identify which users are likely to leave our service so we can better support them."
}'
```

### 2\. Analyze Response

The API structures the problem into a clear, actionable description.

```json
{
  "problem_id": "P8062",
  "description": "Develop a smarter mobile health platform for Northern Ghana to predict high-risk pregnancies, communicate in local languages, and identify users at risk of leaving the service.",
  "clarifying_questions": []
}
```

### 3\. Recommend Request

The structured problem is sent back to the API to generate a solution.

```bash
curl -X POST "http://127.0.0.1:8000/recommend" \
-H "Content-Type: application/json" \
-d '{
  "problem_id": "P8062",
  "description": "Develop a smarter mobile health platform for Northern Ghana to predict high-risk pregnancies, communicate in local languages, and identify users at risk of leaving the service.",
  "clarifying_questions": []
}'
```

### 4\. Recommend Response

The final recommendation is informed by the Jacaranda Health case study in the knowledge base, providing a context-aware and proven technical roadmap.

```json
{
  "solution_summary": "Develop a mobile health platform for Northern Ghana using AI to predict high-risk pregnancies, support local languages, and identify users at risk of disengagement.",
  "recommended_tech_stack": [
    "Messaging Gateway: Africa's Talking for reliable and cost-effective SMS delivery in Ghana.",
    "Backend: Python with Django for efficient logic and data management.",
    "AI/NLP: Leveraging spaCy for entity recognition and Scikit-learn for predictive modeling.",
    "Database: PostgreSQL for secure handling of patient data.",
    "Dashboard: Metabase for visualizing flagged messages and user engagement."
  ],
  "initial_steps": [
    "Conduct a needs assessment in Northern Ghana to understand local health challenges and user preferences.",
    "Build a language model to support local dialects and languages for effective communication with users.",
    "Develop an AI model using historical data to predict high-risk pregnancies and prioritize interventions.",
    "Implement a user engagement tracking system to identify and support users at risk of leaving the service.",
    "Train and onboard a team of local healthcare professionals to provide timely support and intervention based on AI insights."
  ]
}
```

-----

## Demo Case 2: HelpMum, Nigeria

  - **Project Link**: [https://app.techtotherescue.org/project-brief/rec0Mm2QFLnq7Rcwa](https://app.techtotherescue.org/project-brief/rec0Mm2QFLnq7Rcwa)
  - **Knowledge Base Inspiration**: Ubenwa's AI for Infant Cry Analysis (Nigeria)

### 1\. Analyze Request

This request focuses on empowering healthcare workers with a better tool.

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
-H "Content-Type: application/json" \
-d '{
  "problem_statement": "Our healthcare workers in Nigeria lack the tools to quickly identify high-risk pregnancies. We need an AI-powered system that helps them stratify risk levels early in antenatal care, so they can provide the right tailored support for each mother and prevent complications."
}'
```

### 2\. Analyze Response

The API correctly identifies the core task and asks relevant clarifying questions.

```json
{
  "problem_id": "PBE0C",
  "description": "Developing a system to stratify pregnancy risk levels for early identification and tailored care in Nigerian communities.",
  "clarifying_questions": [
    "What specific risk factors need to be considered in stratifying pregnancy risk levels?",
    "What resources (technological, financial, human) are available for implementing this system?",
    "How will the system integrate with existing healthcare processes and technologies in Nigeria?"
  ]
}
```

### 3\. Recommend Request

The full, structured problem is sent to generate the final recommendation.

```bash
curl -X POST "http://127.0.0.1:8000/recommend" \
-H "Content-Type: application/json" \
-d '{
  "problem_id": "PBE0C",
  "description": "Developing a system to stratify pregnancy risk levels for early identification and tailored care in Nigerian communities.",
  "clarifying_questions": [
    "What specific risk factors need to be considered in stratifying pregnancy risk levels?",
    "What resources (technological, financial, human) are available for implementing this system?",
    "How will the system integrate with existing healthcare processes and technologies in Nigeria?"
  ]
}'
```

### 4\. Recommend Response

Informed by the Ubenwa case study, the recommendation focuses on creating an AI-powered *decision support tool* for professionals on the ground.

```json
{
  "solution_summary": "Develop a free SMS platform that stratifies pregnancy risk levels using AI-powered NLP to provide tailored care and early identification for expectant mothers in Nigerian communities.",
  "recommended_tech_stack": [
    "Messaging Gateway: Africa's Talking for reliable and cost-effective SMS delivery in Nigeria.",
    "Backend: Python with Django for efficient logic and data management.",
    "AI/NLP: spaCy for entity recognition and Scikit-learn for text classification models.",
    "Database: PostgreSQL for secure handling of patient data.",
    "Dashboard: Metabase for the clinical team to view risk levels and patient data."
  ],
  "initial_steps": [
    "Conduct a needs assessment to understand the specific requirements and challenges of expectant mothers in Nigerian communities.",
    "Develop a prototype of the SMS platform with basic features for risk level identification and tailored care messages.",
    "Train the AI model using relevant data to accurately detect danger signs and stratify pregnancy risk levels.",
    "Pilot the platform in a small community to gather feedback and iterate on the system based on user input.",
    "Scale up the platform gradually, ensuring continuous monitoring and evaluation to improve effectiveness and impact."
  ]
}
```
