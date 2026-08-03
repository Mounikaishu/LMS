import streamlit as st
from services.upload_service import process_upload
from services.repository_manager import (
    get_departments,
    get_semesters,
    get_subjects,
    create_subject,
    create_unit,
)

st.title("📚 Faculty Upload")

# -----------------------------
# Department
# -----------------------------
department = st.selectbox(
    "Department",
    get_departments()
)
#-----------------------------
#semester
#-----------------------------
semester = st.selectbox(
    "Semester",
    get_semesters()
)

# -----------------------------
# Subject
# -----------------------------
mode = st.radio(
    "Subject",
    [
        "Existing Subject",
        "Create New Subject"
    ]
)

if mode == "Existing Subject":

    subjects = get_subjects(
        department,
        semester
    )

    if subjects:
        subject = st.selectbox(
            "Subject",
            subjects
        )
    else:
        st.warning("No subjects found. Create one.")
        subject = ""

else:

    subject = st.text_input(
        "New Subject"
    )

# -----------------------------
# Unit
# -----------------------------
unit = st.text_input("Unit Name")

# -----------------------------
# Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload PDF / PPT / DOCX",
    type=["pdf", "ppt", "pptx", "docx"]
)

if st.button("Upload"):

    if not subject:
        st.error("Please enter/select a subject.")

    elif not unit:
        st.error("Please enter a unit.")

    elif uploaded_file is None:
        st.error("Please upload a file.")

    else:

        output_file = process_upload(
            uploaded_file,
            department,
            semester,
            subject,
            unit
        )

        st.success("✅ Upload Successful!")

        st.write("Markdown Saved To:")

        st.code(str(output_file))