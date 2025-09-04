# API Demo Cases

This document provides concrete examples of the end-to-end workflow for the AI Architect API, from an initial problem statement to a full technical recommendation.

-----

## Demo Case 1: Savana Signatures, Ghana

  * **Project Link**: [https://app.techtotherescue.org/project-brief/recTLXFImjilnKyz4](https://app.techtotherescue.org/project-brief/recTLXFImjilnKyz4)

### 1\. Analyze Request

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
-H "Content-Type: application/json" \
-d '{
  "problem_statement": "We operate in Northern Ghana, where many expectant mothers and their children face a high risk of preventable death due to a lack of access to consistent, quality healthcare. Our existing mobile health platforms, T4MCH and SHE+, are struggling to keep up. We have a lot of valuable data, but we can'\''t effectively use it to see which pregnancies are high-risk until it'\''s too late. Furthermore, many of our health messages are in English, which doesn'\''t connect with everyone in our diverse communities, and we have a hard time predicting which mothers will stop using our service, leaving them without support. We need a way to make our system smarter so we can proactively identify and intervene with the mothers who need our help the most, communicate with them in their own language, and provide better insights to the Ghana Health Service."
}'
```

### 2\. Analyze Response

```json
{
  "problem_id": "PCD9D",
  "description": "Improving proactive identification and intervention for high-risk pregnancies and enhancing user engagement in Northern Ghana.",
  "clarifying_questions": [
    "What specific data points are currently being collected through the existing platforms?",
    "What languages are predominantly spoken in the communities served?",
    "What are the current methods of communication and engagement with expectant mothers?"
  ]
}
```

### 3\. Recommend Request

```bash
curl -X POST "http://127.0.0.1:8000/recommend" \
-H "Content-Type: application/json" \
-d '{
  "problem_id": "PCD9D",
  "description": "Improving proactive identification and intervention for high-risk pregnancies and enhancing user engagement in Northern Ghana.",
  "clarifying_questions": [
    "What specific data points are currently being collected through the existing platforms?",
    "What languages are predominantly spoken in the communities served?",
    "What are the current methods of communication and engagement with expectant mothers?"
  ]
}'
```

### 4\. Recommend Response

```json
{
  "solution_summary": "Implement a mobile health application that utilizes AI for proactive identification of high-risk pregnancies and enhances user engagement in Northern Ghana.",
  "recommended_tech_stack": [
    "Mobile app development: Flutter",
    "AI/ML: TensorFlow Lite",
    "Database: Firebase",
    "Messaging: Twilio",
    "User engagement: Firebase Cloud Messaging"
  ],
  "initial_steps": [
    "Conduct a needs assessment to understand the specific requirements and challenges in Northern Ghana",
    "Develop a prototype of the mobile health application with basic features for proactive identification of high-risk pregnancies",
    "Pilot test the application with a small group of users to gather feedback and iterate on the design",
    "Integrate AI/ML algorithms for risk assessment and user engagement features into the application",
    "Train local healthcare workers on using the application and provide support for scaling up usage"
  ]
}
```

-----

## Demo Case 2: HelpMum, Nigeria

  * **Project Link**: [https://app.techtotherescue.org/project-brief/rec0Mm2QFLnq7Rcwa](https://app.techtotherescue.org/project-brief/rec0Mm2QFLnq7Rcwa)

### 1\. Analyze Request

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
-H "Content-Type: application/json" \
-d '{
  "problem_statement": "In the communities we serve across Nigeria, far too many mothers are dying from preventable pregnancy-related complications. Our healthcare workers on the ground, including midwives and community health experts, are doing their best, but they lack the tools to effectively and quickly identify which pregnancies are high-risk before a crisis occurs. We have a vision for a system that can help them stratify risk levels as soon as a woman enters antenatal care, but we don'\''t know how to build it. We need a way to empower our healthcare professionals with a tool that helps them assess risk early, categorize pregnancies accurately, and provide the right tailored care for each mother depending on her specific situation and trimester."
}'
```

### 2\. Analyze Response

```json
{
  "problem_id": "P3072",
  "description": "Developing a system to stratify pregnancy risk levels and provide tailored care for high-risk pregnancies in Nigerian communities.",
  "clarifying_questions": [
    "What specific risk factors need to be considered in categorizing pregnancies?",
    "What resources (technological, financial, human) are available for implementing this system?",
    "How will the system integrate with existing healthcare infrastructure and workflows?"
  ]
}
```

### 3\. Recommend Request & Response

*Note: The user did not provide a separate request for this step, only the final response.*

```json
{
  "solution_summary": "Implement a web-based platform that stratifies pregnancy risk levels using machine learning algorithms and provides tailored care recommendations for high-risk pregnancies in Nigerian communities.",
  "recommended_tech_stack": [
    "Python",
    "Django",
    "Scikit-learn",
    "HTML/CSS",
    "JavaScript"
  ],
  "initial_steps": [
    "Gather historical pregnancy data from local healthcare facilities",
    "Identify key risk factors for high-risk pregnancies in Nigerian context",
    "Develop machine learning models to stratify pregnancy risk levels",
    "Design and develop a web platform for inputting patient data and receiving tailored care recommendations"
  ]
}
```

-----

## Demo Case 3: Dignitas Project, Kenya

  * **Project Link**: [https://app.techtotherescue.org/project-brief/recYeqmGhwDQhcgPl](https://app.techtotherescue.org/project-brief/recYeqmGhwDQhcgPl)

### 1\. Analyze Request

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
-H "Content-Type: application/json" \
-d '{
  "problem_statement": "We are facing a critical issue in Kenya where a majority of students are not meeting basic learning levels, and we'\''ve identified that the quality of teaching is the primary driver. Teachers, especially in underserved communities, are not getting the continuous, effective professional development they need to master their subjects and improve their classroom practices. While our '\''LeadNow'\'' platform was built to provide remote training and coaching, we'\''re finding it difficult to scale our support in a meaningful way. We can'\''t offer personalized learning paths to every educator, our feedback is not as immediate or data-driven as it needs to be, and we struggle to identify which school leaders are falling behind or might stop using the platform. We need to find a way to transform our one-size-fits-all approach into a more dynamic, responsive, and personalized coaching system that can truly elevate teaching quality across the country."
}'
```

### 2\. Analyze Response & Recommendation

*Note: The user did not provide separate requests and responses for this case, only the final recommendation.*

```json
{
  "solution_summary": "Implement a personalized coaching system using a combination of online platforms, video conferencing tools, and data analytics to improve teaching quality in Kenya.",
  "recommended_tech_stack": [
    "Google Forms",
    "Zoom",
    "Google Sheets",
    "Microsoft Power BI"
  ],
  "initial_steps": [
    "Conduct a needs assessment to identify specific areas for improvement in teaching practices.",
    "Develop personalized coaching modules based on identified needs.",
    "Train coaches on using online platforms like Google Forms for data collection and analysis.",
    "Pilot the coaching system with a small group of teachers to gather feedback and make necessary adjustments."
  ]
}
```