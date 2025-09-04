import streamlit as st
import streamlit_survey as ss
from survey_questions import SURVEY_QUESTIONS
from scoring import calculate_category_scores, calculate_overall_score, get_readiness_level
from recommendations import get_recommendations
from llm_report import generate_llm_report

st.set_page_config(page_title="AI Readiness Assessment", layout="centered")

# Initialize session state using dictionary-style access.
if "survey_completed" not in st.session_state:
    st.session_state["survey_completed"] = False
    st.session_state["survey_data"] = None

# --- Main Application Logic ---
st.title("Nonprofit AI Readiness Assessment Tool")

survey = ss.StreamlitSurvey()

# --- Callback function to run upon survey submission ---
def handle_submit():
    """
    This function is called when the user clicks the 'Submit' button on the last page.
    It saves the survey data and sets the completion flag in the session state.
    """
    st.session_state["survey_data"] = survey.data
    st.session_state["survey_completed"] = True

# If the survey is NOT completed, display the survey
if not st.session_state["survey_completed"]:
    st.markdown("This tool helps nonprofit organizations understand their readiness for adopting AI. The survey takes less than 10 minutes to complete.")
    st.markdown("---")
    
    pages = survey.pages(len(SURVEY_QUESTIONS), on_submit=handle_submit)

    with pages:
        if pages.current == 0:
            st.subheader("Digital Infrastructure")
            for q in SURVEY_QUESTIONS["Digital Infrastructure"]:
                st.markdown(f"#### {q['question']}")
                survey.radio(label=q["question"], options=list(q["options"].values()), id=q["id"], horizontal=False, label_visibility="collapsed")
        
        elif pages.current == 1:
            st.subheader("Leadership & Culture")
            for q in SURVEY_QUESTIONS["Leadership & Culture"]:
                st.markdown(f"#### {q['question']}")
                survey.radio(label=q["question"], options=list(q["options"].values()), id=q["id"], horizontal=False, label_visibility="collapsed")

        elif pages.current == 2:
            st.subheader("Staff Capacity")
            for q in SURVEY_QUESTIONS["Staff Capacity"]:
                st.markdown(f"#### {q['question']}")
                survey.radio(label=q["question"], options=list(q["options"].values()), id=q["id"], horizontal=False, label_visibility="collapsed")
        
        elif pages.current == 3:
            st.subheader("Data Readiness")
            for q in SURVEY_QUESTIONS["Data Readiness"]:
                st.markdown(f"#### {q['question']}")
                survey.radio(label=q["question"], options=list(q["options"].values()), id=q["id"], horizontal=False, label_visibility="collapsed")
        
        elif pages.current == 4:
            st.subheader("Financial Resources")
            for q in SURVEY_QUESTIONS["Financial Resources"]:
                st.markdown(f"#### {q['question']}")
                survey.radio(label=q["question"], options=list(q["options"].values()), id=q["id"], horizontal=False, label_visibility="collapsed")
        
        elif pages.current == 5:
            st.subheader("Use Case Clarity")
            for q in SURVEY_QUESTIONS["Use Case Clarity"]:
                st.markdown(f"#### {q['question']}")
                survey.radio(label=q["question"], options=list(q["options"].values()), id=q["id"], horizontal=False, label_visibility="collapsed")

# If the survey IS completed, display the report
else:
    st.success("Thank you for completing the assessment! Here is your report.")
    st.markdown("---")
    st.header("Your AI Readiness Report")

    if st.session_state["survey_data"]:
        formatted_responses = {}
        for category, questions in SURVEY_QUESTIONS.items():
            for q in questions:
                question_id = q['id']
                if question_id in st.session_state["survey_data"]:
                    question_text = q['question']
                    question_key = f"{category} - {question_text}"
                    formatted_responses[question_key] = st.session_state["survey_data"][question_id].get('value')

        # 1. Calculate Scores
        category_scores = calculate_category_scores(formatted_responses, SURVEY_QUESTIONS)
        overall_score = calculate_overall_score(category_scores)
        readiness_level, readiness_description = get_readiness_level(overall_score)
        
        # 2. Generate Recommendations
        recommendations = get_recommendations(category_scores)

        # 3. Display Executive Summary
        st.subheader("Executive Summary")
        st.metric(label="Overall AI Readiness Score", value=f"{overall_score}/100")
        st.markdown(f"**Your Readiness Level is: {readiness_level}**")
        st.write(readiness_description)
        
        st.markdown("---")

        # 4. Display Category Breakdown
        st.subheader("Category Breakdown & Recommendations")
        for category, score in category_scores.items():
            st.markdown(f"**{category}**")
            st.progress(int(score))
            with st.expander("View Recommendations"):
                recs = recommendations.get(category, [])
                if recs:
                    for rec in recs:
                        st.markdown(f"- {rec}")
                else:
                    st.write("You are doing great in this area!")
        
        st.markdown("---")

        # 5. Add button to generate LLM report
        st.subheader("Generate Narrative Report")
        if st.button("Create Human-Readable Report with LLM"):
            with st.spinner("✍️ Our AI strategist is writing your personalized report..."):
                llm_generated_report = generate_llm_report(
                    overall_score,
                    readiness_level,
                    readiness_description,
                    category_scores,
                    recommendations
                )
                st.markdown(llm_generated_report)
    else:
        st.error("Could not load survey data. Please try completing the survey again.")
        