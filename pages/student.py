import streamlit as st

from services.github_index_reader import (
    load_index,
    get_departments,
    get_semesters,
    get_subjects,
    get_units,
)

from services.github_reader import get_markdown

st.title("📖 Student Notes")

# -----------------------------
# Load index.json
# -----------------------------
data = load_index()

if not data:
    st.error("Unable to load repository index.")
    st.stop()

# -----------------------------
# Department
# -----------------------------
departments = get_departments(data)

department = st.selectbox(
    "Department",
    departments
)



# -----------------------------
# Semester
# -----------------------------
semesters = get_semesters(data, department)


if not semesters:
    st.warning("No semesters found.")
    st.stop()

semester = st.selectbox(
    "Semester",
    semesters
)



# -----------------------------
# Subject
# -----------------------------
subjects = get_subjects(data, department, semester)


if not subjects:
    st.warning("No subjects found.")
    st.stop()

subject = st.selectbox(
    "Subject",
    subjects
)



# -----------------------------
# Unit
# -----------------------------
units = get_units(data, department, semester, subject)

if not units:
    st.warning("No units found.")
    st.stop()

unit = st.selectbox(
    "Unit",
    units
)

# -----------------------------
# View Notes
# -----------------------------
if st.button("View Notes"):

    markdown = get_markdown(
        department,
        semester,
        subject,
        unit
    )

    if markdown:
         with st.container(border=True):
           st.markdown(markdown)
    else:
         st.error("Notes not found.")