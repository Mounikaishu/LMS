import streamlit as st
from pathlib import Path

from upload import upload_material
from config import REPOSITORY

st.set_page_config(
    page_title="College LMS",
    layout="wide"
)

st.title("📚 College Learning Management System")

menu = st.sidebar.radio(
    "Select Module",
    [
        "Faculty Upload",
        "Student View"
    ]
)

#####################################################
# FACULTY
#####################################################

if menu == "Faculty Upload":

    st.header("Faculty Upload")

    department = st.selectbox(
        "Department",
        [
            "IT",
            "CSE",
            "ECE",
            "AI-DS"
        ]
    )

    semester = st.selectbox(
        "Semester",
        [
            "1","2","3","4","5","6","7","8"
        ]
    )

    subject = st.text_input("Subject")

    unit = st.text_input("Unit")

    uploaded_file = st.file_uploader(
        "Choose File",
        type=[
            "pdf",
            "pptx",
            "docx"
        ]
    )

    if st.button("Upload"):

        if uploaded_file is None:
            st.error("Please upload a document.")

        elif subject == "":
            st.error("Enter Subject")

        elif unit == "":
            st.error("Enter Unit")

        else:

            markdown_file = upload_material(
                department,
                semester,
                subject,
                unit,
                uploaded_file
            )

            st.success("Upload Successful")

            st.write(markdown_file)

#####################################################
# STUDENT
#####################################################

else:

    st.header("Student View")

    department = st.selectbox(
        "Department",
        [
            "IT",
            "CSE",
            "ECE",
            "AI-DS"
        ]
    )

    semester = st.selectbox(
        "Semester",
        [
            "1","2","3","4","5","6","7","8"
        ]
    )

    subject = st.text_input("Subject")

    unit = st.text_input("Unit")

    if st.button("View Notes"):

        markdown_path = (
            REPOSITORY
            / department
            / f"Semester{semester}"
            / subject
            / f"{unit}.md"
        )

        if markdown_path.exists():

            with open(
                markdown_path,
                "r",
                encoding="utf-8"
            ) as f:

                markdown = f.read()

            st.markdown(markdown)

        else:

            st.error("Notes not found.")