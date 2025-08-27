import os
from datetime import datetime

import streamlit as st

from water_sanitation_crew.crew import WaterSanitationCrew


def run_crew_with_topic(topic: str) -> str:
    inputs = {
        "topic": topic,
        "current_year": str(datetime.now().year),
    }

    WaterSanitationCrew().crew().kickoff(inputs=inputs)

    report_path = os.path.join(os.getcwd(), "report.md")
    if not os.path.exists(report_path):
        return "No report generated."
    with open(report_path, "r", encoding="utf-8") as f:
        return f.read()


st.set_page_config(page_title="Water & Sanitation Planner", page_icon="🚰", layout="wide")
st.title("Water & Sanitation Planner 🚰")
st.write("Enter community details, then generate a tailored water & sanitation report.")

st.sidebar.header("Configuration")
api_key_input = st.sidebar.text_input("Gemini API Key", type="password", help="Used to run the AI agents. Not stored.")
if api_key_input:
    # CrewAI/LiteLLM expects GOOGLE_API_KEY for Gemini
    os.environ["GOOGLE_API_KEY"] = api_key_input
    # Some providers/tools expect GEMINI_API_KEY as well
    os.environ["GEMINI_API_KEY"] = api_key_input

with st.form("community_form"):
    community_name = st.text_input("Community name", placeholder="e.g., Kachia, Kaduna State")
    population = st.text_input("Population (approx)", placeholder="e.g., 500 residents")
    sanitation_gap = st.text_input("% without toilets", placeholder="e.g., 70% without toilets")
    water_source = st.text_input("Current water source", placeholder="e.g., Rely on streams")
    submitted = st.form_submit_button("Generate Report")

if submitted:
    has_any_key = (
        os.environ.get("GOOGLE_API_KEY")
        or os.environ.get("GEMINI_API_KEY")
    )
    if not has_any_key:
        st.error("Missing API key. Provide it in the left sidebar or set GOOGLE_API_KEY or GEMINI_API_KEY.")
    elif not community_name:
        st.error("Please provide the community name.")
    else:
        topic_parts = [
            f"Community: {community_name}" if community_name else "",
            population if population else "",
            sanitation_gap if sanitation_gap else "",
            water_source if water_source else "",
        ]
        topic = ". ".join([p.strip().rstrip('.') for p in topic_parts if p.strip()]) + "."

        with st.spinner("Running agents and generating report..."):
            report_md = run_crew_with_topic(topic)

        st.success("Report generated.")
        st.download_button(
            label="Download report.md",
            data=report_md,
            file_name="report.md",
            mime="text/markdown",
        )
        st.divider()
        st.subheader("Preview")
        st.markdown(report_md)


