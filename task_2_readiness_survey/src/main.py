import streamlit as st
import streamlit_survey as ss

from survey_questions import SURVEY_QUESTIONS
from scoring import calculate_category_scores, calculate_overall_score, get_readiness_level
from recommendations import get_recommendations
from llm_report import generate_llm_report

st.set_page_config(page_title="AI Readiness Assessment", layout="centered")

# Initialize session state
if "survey_completed" not in st.session_state:
    st.session_state["survey_completed"] = False
    st.session_state["survey_data"] = None
if "llm_report" not in st.session_state:
    st.session_state["llm_report"] = None

# --- Main Application Logic ---
st.title("💡 Nonprofit AI Readiness Companion")

survey = ss.StreamlitSurvey()

# --- Callback for survey submission ---
def handle_submit():
    """Saves the survey data and marks the completion flag."""
    st.session_state["survey_data"] = survey.data
    st.session_state["survey_completed"] = True

# --- Helper to create markdown report ---
def create_markdown_report(report_text: str) -> str:
    """
    Takes the report text and formats it for download as a Markdown file.
    """
    return report_text

# --- Survey view ---
if not st.session_state["survey_completed"]:
    st.markdown(
        "🌍 Welcome! This quick assessment (under 10 minutes) is designed to help your "
        "organization explore where you are on your AI journey. "
        "There are **no right or wrong answers** — just an opportunity to reflect. "
        "Your responses will guide supportive, practical recommendations."
    )
    st.markdown("---")

    pages = survey.pages(len(SURVEY_QUESTIONS), on_submit=handle_submit)

    with pages:
        if pages.current == 0:
            st.subheader("🖥️ Digital Infrastructure")
            st.info(
                "Every organization has a different starting point with technology. "
                "This section looks at the tools and systems you’re currently using."
            )
            for q in SURVEY_QUESTIONS["Digital Infrastructure"]:
                st.markdown(f"#### {q['question']}")
                survey.radio(
                    label=q["question"],
                    options=list(q["options"].values()),
                    id=q["id"],
                    horizontal=False,
                    label_visibility="collapsed"
                )

        elif pages.current == 1:
            st.subheader("🤝 Leadership & Culture")
            st.info(
                "Leadership support and organizational culture shape how easily new ideas take root. "
                "Here we’ll explore how leadership currently views technology and innovation."
            )
            for q in SURVEY_QUESTIONS["Leadership & Culture"]:
                st.markdown(f"#### {q['question']}")
                survey.radio(
                    label=q["question"],
                    options=list(q["options"].values()),
                    id=q["id"],
                    horizontal=False,
                    label_visibility="collapsed"
                )

        elif pages.current == 2:
            st.subheader("👩‍💻 Staff Capacity")
            st.info(
                "Technology is only as strong as the people who use it. "
                "This section looks at your team’s comfort with technology and learning opportunities."
            )
            for q in SURVEY_QUESTIONS["Staff Capacity"]:
                st.markdown(f"#### {q['question']}")
                survey.radio(
                    label=q["question"],
                    options=list(q["options"].values()),
                    id=q["id"],
                    horizontal=False,
                    label_visibility="collapsed"
                )

        elif pages.current == 3:
            st.subheader("📊 Data Readiness")
            st.info(
                "Good data makes AI powerful. This section is about how your organization "
                "stores, manages, and ensures the quality of data."
            )
            for q in SURVEY_QUESTIONS["Data Readiness"]:
                st.markdown(f"#### {q['question']}")
                survey.radio(
                    label=q["question"],
                    options=list(q["options"].values()),
                    id=q["id"],
                    horizontal=False,
                    label_visibility="collapsed"
                )

        elif pages.current == 4:
            st.subheader("💰 Financial Resources")
            st.info(
                "Investing in technology doesn’t always mean big budgets — "
                "it’s about how resources are planned and prioritized. "
                "This section explores how funding for technology is approached."
            )
            for q in SURVEY_QUESTIONS["Financial Resources"]:
                st.markdown(f"#### {q['question']}")
                survey.radio(
                    label=q["question"],
                    options=list(q["options"].values()),
                    id=q["id"],
                    horizontal=False,
                    label_visibility="collapsed"
                )

        elif pages.current == 5:
            st.subheader("🎯 Use Case Clarity")
            st.info(
                "Clear use cases help focus energy where AI can add the most value. "
                "Here we’ll look at how clearly your organization has identified opportunities for AI."
            )
            for q in SURVEY_QUESTIONS["Use Case Clarity"]:
                st.markdown(f"#### {q['question']}")
                survey.radio(
                    label=q["question"],
                    options=list(q["options"].values()),
                    id=q["id"],
                    horizontal=False,
                    label_visibility="collapsed"
                )

# --- Report view ---
else:
    st.success("✅ Thank you for sharing your insights!")
    st.header("📖 Your Personalized AI Readiness Report")
    st.markdown(
        "This report is designed to celebrate your strengths and highlight areas where "
        "small steps could create big impact. Think of it as a **roadmap, not a scorecard.**"
    )
    st.markdown("---")

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
        st.subheader("🌟 Executive Summary")
        st.metric(label="Overall AI Readiness Snapshot", value=f"{overall_score}/100")
        st.markdown(f"✨ You are currently at the **{readiness_level}** stage.")
        st.write(readiness_description)

        st.markdown("---")

        # 4. Display Category Breakdown
        st.subheader("🔎 Category Breakdown & Recommendations")
        for category, score in category_scores.items():
            st.markdown(f"### {category}")
            st.progress(int(score))
            st.caption("This bar shows your current progress in this area — every organization starts somewhere.")
            with st.expander("💡 Recommendations"):
                recs = recommendations.get(category, [])
                if recs:
                    for rec in recs:
                        st.markdown(f"- {rec}")
                else:
                    st.write("👏 You’re already in a strong place here!")

        st.markdown("---")

        # 5. Add button to generate LLM report
        st.subheader("📝 Create a Narrative Report")
        st.caption("Our AI strategist will write a plain-language summary tailored to your results.")
        if st.button("Generate My Report"):
            with st.spinner("✍️ Writing your personalized report..."):
                llm_generated_report = generate_llm_report(
                    overall_score,
                    readiness_level,
                    readiness_description,
                    category_scores,
                    recommendations
                )
                st.session_state["llm_report"] = llm_generated_report
                st.markdown(llm_generated_report)

        # 6. Download as Markdown if report exists
        if st.session_state.get("llm_report"):
            markdown_report = create_markdown_report(st.session_state["llm_report"])
            st.download_button(
                label="📥 Download Report as Markdown",
                data=markdown_report,
                file_name="AI_Readiness_Report.md",
                mime="text/markdown"
            )

    else:
        st.error("⚠️ Could not load survey data. Please try completing the survey again.")
        