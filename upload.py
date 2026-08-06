from pathlib import Path

from config import REPOSITORY, TEMP_FOLDER
from converter import convert_to_markdown
from git_manager import push_changes
from services.index_service import save_index


def upload_material(
    department,
    semester,
    subject,
    unit,
    uploaded_file
):
    """
    Upload a faculty document to the repository.

    uploaded_file is the object returned by
    st.file_uploader().
    """

    # -------------------------
    # Repository Path
    # -------------------------

    destination_folder = (
        REPOSITORY
        / department
        / f"Semester{semester}"
        / subject
    )

    destination_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    # -------------------------
    # Save uploaded document temporarily
    # -------------------------

    temp_file = TEMP_FOLDER / uploaded_file.name

    with open(temp_file, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # -------------------------
    # Markdown destination
    # -------------------------

    markdown_file = destination_folder / f"{unit}.md"

    # -------------------------
    # Convert using Docling
    # -------------------------

    convert_to_markdown(
        temp_file,
        markdown_file
    )
    save_index(REPOSITORY)
    # -------------------------
    # Delete temporary file
    # -------------------------

    temp_file.unlink()

    # -------------------------
    # Push changes
    # -------------------------

    commit_message = (
        f"{department} | "
        f"Semester {semester} | "
        f"{subject} | "
        f"{unit}"
    )

    push_changes(
        REPOSITORY,
        commit_message
    )

    return markdown_file