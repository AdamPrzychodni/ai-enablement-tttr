# Task 2: AI Readiness Assessment Tool - Requirements Documentation

## Overview
Build a tool that assesses nonprofit organizations' readiness for AI transformation through a structured survey, scoring system, and recommendation engine.

## Core Requirements

### Survey Design Requirements
- **Structure**: 5-7 core readiness categories
- **Completion Time**: Maximum 10 minutes
- **Question Types**: 0-10 scale, Likert scale, or multiple choice
- **Coverage Areas**: Must probe important readiness factors:
  - Digital infrastructure
  - Leadership commitment
  - Staff capacity
  - Budget/resources
  - Data maturity
  - Current technology usage
  - Organizational culture

### Scoring System Requirements
- **Category Scores**: Individual scoring for each readiness area
- **Overall Score**: Aggregated readiness level calculation
- **Scoring Logic**: Clear documentation of:
  - How category scores are calculated
  - How overall scores are derived
  - Thresholds for each readiness level
- **Readiness Levels**: Define meaningful tiers (e.g., "Needs Foundation", "Emerging", "Ready", "Advanced")

### Tool Specifications
- **Input Formats**: Accept survey responses via:
  - JSON format
  - CSV format
  - Web form (if web app implementation)
- **Processing**: Calculate scores based on defined rubric
- **Output Requirements**:
  - Category-specific scores
  - Overall readiness level
  - Actionable recommendations per category
  - Human-readable report format (Markdown or PDF)

## Deliverables Checklist

### Survey Documentation
- Complete survey questions organized by category
- Scoring rubric with weighted calculations
- Scoring table showing point allocations
- Rationale for each category's importance
- Mapping between scores and readiness levels

### Tool Implementation
- Source code for scoring tool (CLI, script, or web app)
- Input validation and error handling
- Score calculation logic
- Report generation functionality
- README with installation and usage instructions

### Demo Materials
- Two example assessments:
  - "AI Ready" organization example
  - "Needs Foundation" organization example
- Corresponding generated reports for each
- Sample data files (JSON/CSV format)

### Recommendation Framework
- Templates for each readiness level
- Category-specific improvement suggestions
- Actionable next steps based on scores
- Resource recommendations appropriate to nonprofit constraints

### Integration Documentation
- How the assessment plugs into TTTR onboarding
- Connection to consultation processes
- Workflow for using assessment results
- Guidelines for interpreting scores

## Technical Stack Options
- **CLI Implementation**: Python/Node.js script
- **Web App**: Streamlit, Flask, or FastAPI with frontend
- **Report Generation**: Markdown, PDF (using libraries like ReportLab)
- **Data Processing**: pandas, numpy for analysis
- **Visualization**: matplotlib, plotly for score visualization

## Evaluation Criteria Focus

### Quality of Survey (25%)
- Relevance of categories to nonprofit AI readiness
- Clarity and appropriateness of questions
- Coverage of critical readiness factors
- Balance between comprehensiveness and brevity

### Scoring Methodology (25%)
- Practicality of scoring rules
- Insightfulness of rubric design
- Meaningful differentiation between levels
- Validity of assessment approach

### Technical Implementation (20%)
- Code clarity and organization
- Ease of use and installation
- Error handling and validation
- Report quality and formatting

### Recommendations Quality (20%)
- Actionability of suggestions
- Context-awareness for nonprofits
- Appropriateness to readiness level
- Practical next steps

### Documentation (10%)
- Strategic fit with TTTR processes
- Clarity of instructions
- Completeness of materials
- Integration guidance

## Required Categories Examples

### Suggested Assessment Categories
1. **Digital Infrastructure**
   - Current technology stack
   - Data management systems
   - Cloud adoption level
   - IT support availability

2. **Leadership & Culture**
   - Executive buy-in for AI
   - Innovation mindset
   - Change management readiness
   - Strategic planning maturity

3. **Staff Capacity**
   - Technical skills present
   - Training resources
   - Data literacy levels
   - Time for learning

4. **Data Readiness**
   - Data quality and availability
   - Data governance practices
   - Privacy/security measures
   - Historical data access

5. **Financial Resources**
   - Budget for technology
   - Funding stability
   - ROI understanding
   - Resource allocation flexibility

6. **Use Case Clarity**
   - Problem identification
   - Success metrics defined
   - Impact measurement capability
   - Pilot project readiness

7. **External Support** (optional)
   - Partner ecosystem
   - Vendor relationships
   - Community connections
   - Technical assistance access

## Scoring Logic Requirements

### Score Calculation
- Define point values for each question
- Specify weighting for categories
- Document aggregation method
- Create clear threshold definitions

### Example Scoring Structure
```
Category Score = (Sum of Question Points / Maximum Possible) * 100
Overall Score = Weighted Average of Category Scores

Readiness Levels:
- 0-25: Foundational (needs basic digital infrastructure)
- 26-50: Emerging (building capabilities)
- 51-75: Ready (prepared for AI adoption)
- 76-100: Advanced (optimized for AI transformation)
```

## Report Requirements

### Report Structure
1. **Executive Summary**
   - Overall readiness level
   - Key strengths
   - Priority improvement areas

2. **Category Breakdown**
   - Individual scores
   - Specific findings
   - Targeted recommendations

3. **Action Plan**
   - Immediate next steps
   - 3-6 month goals
   - Long-term objectives
   - Resource requirements

4. **Resources**
   - Relevant tools/platforms
   - Training opportunities
   - Funding sources
   - TTTR programs alignment

## Repository Structure Requirements

```
task_2_readiness_survey/
├── src/                    # Source code for scoring tool
├── example_reports/        # Two example assessment reports
├── data/                   # Sample input files
├── templates/             # Recommendation templates
├── .env.example           # If using LLM for recommendations
├── requirements.txt       # Dependencies
├── FRAMEWORK.md          # Detailed survey and scoring logic
└── README.md             # Setup and usage instructions
```

## Testing Requirements

### Required Functionality
- Process sample JSON input
- Process sample CSV input
- Generate scores correctly
- Produce readable reports
- Handle edge cases (missing data, invalid inputs)

### Test Commands
```bash
# Installation
pip install -r requirements.txt

# Run assessment
python src/assessment_tool.py --input data/sample_ready.json
python src/assessment_tool.py --input data/sample_foundation.csv

# Generate report
python src/assessment_tool.py --input data/sample.json --output report.md
```

## Critical Success Factors
1. **Nonprofit Relevance**: Questions and categories meaningful to sector
2. **Practical Scoring**: Rubric that accurately reflects readiness
3. **Actionable Output**: Recommendations nonprofits can implement
4. **Easy Administration**: Simple for nonprofits to complete
5. **TTTR Integration**: Clear fit with organizational processes
6. **Scalability**: Applicable to diverse nonprofit types and sizes

## Constraints
- Survey completion in 10 minutes maximum
- Appropriate for varying technical literacy levels
- Considers nonprofit resource limitations
- Provides value regardless of score
- Maintains encouraging, supportive tone
