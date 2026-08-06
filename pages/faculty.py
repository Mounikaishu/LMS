import streamlit as st
from services.upload_service import process_upload
from services.github_index_reader import load_index

st.title("📚 Faculty Upload")

# -----------------------------
# Load index
# -----------------------------
data = load_index()

departments = sorted(data.keys())

department = st.selectbox(
    "Department",
    departments
)

# -----------------------------
# Semester
# -----------------------------
semesters = list(data.get(department, {}).keys())

semester_options = semesters + ["Create New Semester"]

semester = st.selectbox(
    "Semester",
    semester_options
)

if semester == "Create New Semester":
    semester = st.text_input("Semester Name")

# -----------------------------
# Subject
# -----------------------------
subjects = list(
    data.get(department, {})
        .get(semester, {})
        .keys()
)

mode = st.radio(
    "Subject",
    [
        "Existing Subject",
        "Create New Subject"
    ]
)

if mode == "Existing Subject":

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
# Upload File
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload PDF / PPT / DOCX",
    type=["pdf", "ppt", "pptx", "docx"]
)

# -----------------------------
# Upload Button
# -----------------------------
if st.button("Upload"):

    if not semester:
        st.error("Please enter a semester.")

    elif not subject:
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
        st.write("Markdown saved to:")
        st.code(str(output_file))