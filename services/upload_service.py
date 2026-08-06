from pathlib import Path
import shutil
from services.git_manager import git_push
from services.index_service import save_index

from config import (
    UPLOAD_FOLDER,
    TEMP_FOLDER,
    REPOSITORY,
)

from services.converter import convert_to_markdown


def save_uploaded_file(uploaded_file):

    destination = UPLOAD_FOLDER / uploaded_file.name

    with open(destination, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return destination
def markdown_output_path(
    department,
    semester,
    subject,
    unit
):

    folder = (
        REPOSITORY
        / department
        / semester
        / subject
    )

    folder.mkdir(
        parents=True,
        exist_ok=True
    )

    return folder / f"{unit}.md"
def process_upload(
    uploaded_file,
    department,
    semester,
    subject,
    unit
):

    pdf_path = save_uploaded_file(uploaded_file)

    output_md = markdown_output_path(
        department,
        semester,
        subject,
        unit
    )

    convert_to_markdown(
    pdf_path,
    output_md
)
    print("REPOSITORY =", REPOSITORY)
    save_index(REPOSITORY)

    git_push(
    f"Added {department} {semester} {subject} {unit}"
)
    if pdf_path.exists():
        pdf_path.unlink()
    return output_md