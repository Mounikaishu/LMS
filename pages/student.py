import streamlit as st
from config import REPOSITORY



from services.repository_manager import (
    get_departments,
    get_semesters,
    get_subjects,
    get_units,
)

from viewer import load_markdown

st.title("📖 Student Notes")
department = st.selectbox(
    "Department",
    get_departments()
)

semester = st.selectbox(
    "Semester",
    get_semesters()
)

subjects = get_subjects(department, semester)

if not subjects:
    st.warning("No subjects found.")
    st.stop()

subject = st.selectbox("Subject", subjects)

units = get_units(department, semester, subject)

if not units:
    st.warning("No units found.")
    st.stop()

unit = st.selectbox("Unit", units)

if st.button("View Notes"):

    markdown = load_markdown(
        department,
        semester,
        subject,
        unit
    )

    if markdown:
        st.markdown(markdown)
    else:
        st.error("Notes not found.")