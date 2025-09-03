# Task 1: AI Architect API - Requirements Documentation

## Overview
Build an API server that translates nonprofit problems into actionable AI solutions through two endpoints: `/analyze` and `/recommend`.

## API Specifications

### `/analyze` Endpoint
**Input:**
```json
{
    "problem_statement": "string"
}
```

**Output:**
```json
{
    "problem_id": "string (e.g., 'P01')",
    "description": "string (concise problem summary)",
    "clarifying_questions": ["array of strings or empty []"]
}
```

### `/recommend` Endpoint
**Input:** Exact output structure from `/analyze`

**Output:**
```json
{
    "solution_summary": "string",
    "recommended_tech_stack": ["array of tools/technologies"],
    "initial_steps": ["array of actionable steps"]
}
```

## Technical Stack
- **Framework**: FastAPI, Flask, or Express
- **LLM**: OpenAI GPT or local model with fallback
- **Environment**: `TTTR_API_KEY`, `TTTR_MODEL="gpt-4"`, `TTTR_TEMPERATURE=0.3`

## Key Requirements
- Valid JSON input/output only
- Clear data contract between endpoints
- Environment variables for API keys (never hardcoded)
- Standard environment compatibility

## Deliverables Checklist

### Code
- Working API server with both endpoints
- LLM integration with proper error handling
- JSON validation
- `.env.example` file

### Documentation (README.md)
- Installation & usage instructions
- curl examples for both endpoints
- JSON schema design critique
- Prompt engineering strategy
- Technical decision rationale

### Demo Cases (2-3 required)
- Problem statement
- `/analyze` output
- Clarifying Q&A
- `/recommend` output

## Evaluation Focus Areas
1. **JSON Schema Design** - Logic of data contract between endpoints
2. **Problem Analysis** - Extracting requirements from vague inputs
3. **Solution Quality** - Practical, nonprofit-appropriate recommendations
4. **Code Quality** - Clean, documented, easy to run
5. **Documentation** - Clear, complete, with good examples

## Required Capabilities

### Problem Analysis
- Extract core problems from vague, unstructured text
- Identify information gaps requiring clarification
- Generate relevant, context-specific questions
- Summarize problems concisely

### Solution Generation
- Recommend appropriate AI tools and technologies
- Consider nonprofit constraints (budget, technical capacity)
- Provide actionable implementation steps
- Explain rationale for recommendations

## JSON Schema Requirements

### Current Required Schema
### Current Required Schema
The provided schema must be implemented as specified:
- Simple, clear field names
- Logical flow from analysis to recommendation
- Extensible structure

### Required Schema Critique
Documentation must include:
- Analysis of strengths and weaknesses
- Alternative design proposals with justification
- Improvements for better usability/extensibility

## Required Demo Cases

### Demo Case Requirements (2-3 cases)
Each demo must demonstrate:
- Original problem statement (vague nonprofit need)
- `/analyze` endpoint processing and output
- Clarifying questions with sample answers
- `/recommend` endpoint processing and output

### Example Problem Domains
- Donor engagement and communication
- Volunteer management
- Program impact measurement
- Resource allocation
- Data management

## Repository Structure Requirements

```
task_1_solution_architect/
├── src/                  # Source code for API server
├── demo_cases/          # 2-3 sample input/output flows
├── .env.example         # Environment variable template
└── README.md           # Complete documentation
```

## Testing Requirements

### Required Test Commands
The solution must support:
```bash
# Installation
pip install -r requirements.txt

# Running the server
[framework-specific command]

# Testing /analyze endpoint
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"problem_statement": "[test input]"}'

# Testing /recommend endpoint  
curl -X POST "http://localhost:8000/recommend" \
  -H "Content-Type: application/json" \
  -d '[analyze output JSON]'
```

## Critical Success Factors
1. **Nonprofit Understanding**: Solutions appropriate for resource-constrained organizations
2. **Clear Data Contract**: Well-designed JSON schema between endpoints
3. **Practical Recommendations**: Actionable, implementable suggestions
4. **Easy Setup**: Must run without complex configuration
5. **Good Documentation**: Clear examples and reasoning