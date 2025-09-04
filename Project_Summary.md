# Task 1: AI Architect API

## Overview
The **AI Architect API** is a specialized tool designed to function as an on-demand "solution architect" for the nonprofit sector. It addresses a critical gap where organizations recognize operational challenges but lack the in-house technical expertise to translate those needs into viable, AI-driven projects. The API provides a structured, two-stage process to transform ambiguous problems into actionable technical blueprints.

## Core Functionality
The system operates through two distinct, interconnected endpoints:

1.  **`/analyze` - The Discovery Phase:** This initial stage acts as a "digital consultant." A nonprofit provides a high-level, often vague, `problem_statement` (e.g., "We struggle with volunteer engagement"). The API uses a Large Language Model (LLM) to dissect this input, identify the core challenge, and reframe it as a concise `description`. Crucially, it also generates a set of `clarifying_questions` to pinpoint information gaps, mimicking the requirements-gathering process of a human architect.

2.  **`/recommend` - The Solutioning Phase:** Once the problem is clearly defined (and potentially refined by answering the clarifying questions), the structured output from the `/analyze` endpoint is passed to the `/recommend` endpoint. This stage generates a practical, nonprofit-aware solution. The output includes a `solution_summary`, a `recommended_tech_stack` that considers budget and usability constraints, and a list of concrete `initial_steps` to demystify the implementation process.

## Strategic Goal 🎯
The ultimate goal of the AI Architect API is to **democratize access to strategic AI planning**. It empowers any nonprofit, regardless of its technical capacity, to move from a pressing need to a well-defined project plan, thereby accelerating the adoption of technology to amplify their mission's impact.

***

# Task 2: AI Readiness Assessment Tool

## Overview
The **AI Readiness Assessment Tool** is a diagnostic platform designed to help nonprofits navigate the complexities of digital transformation. Recognizing that successful AI adoption is built on a strong organizational foundation, this tool provides a comprehensive, 360-degree evaluation of a nonprofit's preparedness. It replaces guesswork with a data-driven analysis, offering a clear and actionable starting point for any AI initiative.

## Core Functionality
The tool operates through a simple yet powerful three-step process:

1.  **The Survey:** An organization completes a concise, 10-minute survey. The questions are strategically designed to cover **5-7 core readiness categories** based on established academic and industry frameworks, including **Data Maturity, Leadership & Culture, Digital Infrastructure, Staff Capacity, and Financial Resources.**

2.  **Scoring and Analysis:** The tool processes the survey responses using a sophisticated, weighted scoring rubric. It calculates an individual score for each category, allowing for granular insight into specific strengths and weaknesses. These are then aggregated into an **overall readiness score** and mapped to a clear, understandable level (e.g., "Foundational," "Emerging," "Ready," "Advanced").

3.  **The Personalized Report:** The final output is a comprehensive, human-readable report. This document goes beyond just numbers; it provides a narrative summary, visualizes the scores, and—most importantly—delivers **actionable recommendations tailored to each category's score.** It outlines priority areas, suggests immediate next steps, and points to relevant resources.

## Strategic Goal 🚀
The primary purpose of this tool is to **empower nonprofits to embark on their AI journey with confidence and strategic clarity**. By providing a detailed, objective snapshot of their current capabilities, it enables them to make informed decisions, allocate resources effectively, and build the foundational capacity required for successful and sustainable AI implementation.