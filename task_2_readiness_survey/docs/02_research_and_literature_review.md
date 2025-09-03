# Research and Literature Review - Task 2: AI Readiness Assessment Tool

## Executive Summary

This literature review synthesizes academic research and industry frameworks to inform the design of an AI Readiness Assessment Tool specifically tailored for nonprofits. The research identifies a clear path for implementation by combining validated academic frameworks for structure, quantitative scoring methodologies for rigor, and sector-specific adaptations for relevance. The review reveals that a hybrid approach—grounded in the comprehensive framework of Jöhnk et al. (2020), the quantitative scoring of Mishra (2024), and the nonprofit-centric models from TechSoup and Data Orchard—provides the strongest foundation for a practical and impactful tool.

## Core Implementation Approaches (For Demo)

### 1. Foundational Assessment Framework

**Source**: Jöhnk et al. (2020) - "Ready or Not, AI Comes— An Interview Study of Organizational AI Readiness Factors"

**Key Innovation**: Provides the most comprehensive academic framework with 5 dimensions, 18 factors, and 58 validated indicators, offering granular assessment capabilities. Its context-agnostic design makes it highly adaptable to nonprofit needs.

**Application to TTTR**: Serves as the primary structural backbone for the assessment. The dimensions (Strategic Alignment, Resources, Knowledge, Culture, Data) map directly to nonprofit operational areas and provide a validated set of questions and indicators for the initial demo.

### 2. Quantitative Scoring Engine

**Source**: Mishra (2024) - "Five Dimensions of AI Readiness (AIR-5D) Framework"

**Key Innovation**: The only academic study identified that uses a validated quantitative scoring methodology. It applies the Analytic Hierarchy Process (AHP) to create weighted dimensions, providing mathematical rigor and a mechanism to integrate stakeholder input into the final score.

**Application to TTTR**: Provides the model for the assessment's scoring engine. We will adapt the 5-point maturity scale (Basic to Optimized) and use the AHP methodology to weight dimensions according to nonprofit priorities, ensuring a defensible and nuanced final readiness score.

### 3. Systematic Assessment Process

**Source**: Aldoseri et al. (2024) - "Methodological Approach to Assessing the Current State of Organizations"

**Key Innovation**: Outlines a holistic, step-by-step process that begins with assessing the current state (processes, systems, data) and systematically identifies gaps and priorities. This approach is ideal for nonprofits with legacy infrastructure and resource constraints.

**Application to TTTR**: Informs the user flow of the tool. The assessment will guide users through an evaluation of their current state before identifying opportunities, ensuring recommendations are grounded in reality and actionable.

## Industry Patterns and Best Practices

### Enterprise-Grade Foundational Models

**McKinsey's AI Quotient (AIQ)**: Demonstrates the value of assessment by correlating high AI readiness with significant financial outperformance. Its six-capability framework provides a comprehensive model for organizational evaluation that can be adapted for nonprofit impact measurement.

**Cisco's AI Readiness Index**: Offers a clear benchmarking model with a 100-point scale and four readiness levels ("Laggards" to "Pacesetters"). This provides an excellent template for classifying nonprofit readiness and showing a clear progression pathway.

### Nonprofit-Specific Solutions

**TechSoup's Digital Assessment Tool (DAT)**: The most relevant sector-specific model, proven effective with organizations where 75% have budgets under $1M. Its focus areas (e.g., communications/fundraising, risk management, culture) are directly applicable to TTTR's target audience.

**Data Orchard's Data Maturity Framework**: A comprehensive nonprofit data assessment tool with a strong open-source model (Creative Commons license). Its five maturity stages ("Unaware" to "Mastering") across seven themes provide an excellent, widely adopted progression model for data readiness.

## Advanced Techniques (Future Recommendations)

### 1. Ethical Framework Integration

**Source**: Nagbøl et al. (2021) - "Designing a Risk Assessment Tool for Artificial Intelligence Systems"

Integrate a dedicated module based on Responsible AI principles (fairness, transparency, accountability). This would allow the assessment to not only gauge technical readiness but also ethical preparedness, a critical factor for maintaining community trust in the nonprofit sector.

### 2. Granular Skills and Literacy Assessment

**Source**: Lo (2024) - "Evaluating AI Literacy in Academic Libraries"

Develop an advanced skills module using the TPACK (Technological, Pedagogical, Content Knowledge) framework. This would provide nonprofits with a detailed analysis of their workforce's AI literacy and generate targeted recommendations for professional development and capacity building.

### 3. Benchmarking and Peer Comparison

**Inspiration**: Cisco AI Readiness Index

Once sufficient data is collected, implement a feature allowing nonprofits to anonymously benchmark their readiness scores against similar organizations (based on size, sector, and geography). This provides valuable context and encourages continuous improvement.

## Key Design Insights

**Focus on a 10-Minute Survey**: Research shows that surveys lasting 7-10 minutes achieve optimal engagement and data quality. This requires a focused design with 3-5 core objectives, efficient question placement, and skip logic to maintain momentum.

**Universal Dimensions with a Nonprofit Lens**: Analysis reveals six universal dimensions (Strategy, Data, Talent, Governance, Operations, Value). The tool's unique value comes from adapting these with nonprofit-specific considerations like **mission alignment**, **stakeholder complexity**, **resource optimization**, and **social impact measurement**.

**Hybrid Scoring for Clarity and Nuance**: The most effective scoring system combines a simple 5-level maturity model for clear progression with a weighted scoring system (AHP) to reflect the unique priorities of each nonprofit.

**Strategic Differentiation Through Specialization**: The tool will stand out by focusing on nonprofit-specific challenges and opportunities, emphasizing resource optimization, connecting AI adoption to mission impact, and leveraging an open-source model inspired by Data Orchard to build community.

## Conclusion

The research provides a clear blueprint for developing a best-in-class AI Readiness Assessment Tool for nonprofits. The core implementation will be built on a hybrid of validated academic frameworks for structure (Jöhnk et al.), quantitative scoring for rigor (Mishra), and practical assessment processes (Aldoseri). By overlaying this foundation with nonprofit-specific industry patterns (TechSoup, Data Orchard) and focusing on key design insights, the tool can provide immediate, actionable value while positioning TTTR for future enhancements like ethical assessments and peer benchmarking.

## References

1. Aldoseri, A., et al. (2024). "Methodological Approach to Assessing the Current State of Organizations for AI-Based Digital Transformation." _Journal of Information Systems Engineering & Management_.
    
2. Jöhnk, J., et al. (2020). "Ready or Not, AI Comes— An Interview Study of Organizational AI Readiness Factors." _Pacific Asia Conference on Information Systems (PACIS) Proceedings_.
    
3. Lo, P. (2024). "Evaluating AI Literacy in Academic Libraries: A Survey Study with a Focus on U.S. Employees." _Journal of Academic Librarianship_.
    
4. Mishra, S. (2024). "Five Dimensions of AI Readiness (AIR-5D) Framework- A Preparedness Assessment Tool for Healthcare Organizations." _Journal of Health Management_.
    
5. Nagbøl, P. R., et al. (2021). "Designing a Risk Assessment Tool for Artificial Intelligence Systems." _Nordic Human-Computer Interaction Conference_.
    
6. Cisco. (2023). "AI Readiness Index."
    
7. Data Orchard. (2023). "Data Maturity Framework 2.1."
    
8. McKinsey & Company. (2023). "The state of AI in 2023: Generative AI’s breakout year."
    
9. TechSoup. (2022). "Digital Assessment Tool (DAT)."