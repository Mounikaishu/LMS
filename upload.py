from pathlib import Path

from config import UPLOAD_FOLDER

from services.converter import convert_to_markdown
from services.git_manager import (
    clone_repository,
    commit_changes,
    push_changes,
    cleanup_repository,
)
from services.index_service import save_index


def save_uploaded_file(uploaded_file):
    """
    Save uploaded file temporarily.
    """

    destination = UPLOAD_FOLDER / uploaded_file.name

    with open(destination, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return destination


def markdown_output_path(
    repo_path,
    department,
    semester,
    subject,
    unit,
):
    """
    Create folder structure inside the cloned repository.
    """

    folder = (
        repo_path
        / department
        / semester
        / subject
    )

    folder.mkdir(
        parents=True,
        exist_ok=True,
    )

    return folder / f"{unit}.md"


def process_upload(
    uploaded_file,
    department,
    semester,
    subject,
    unit,
):

    repo_path = None
    pdf_path = None

    try:

        # -----------------------------
        # Save uploaded PDF temporarily
        # -----------------------------
        pdf_path = save_uploaded_file(uploaded_file)

        # -----------------------------
        # Clone repository
        # -----------------------------
        repo_path = clone_repository()

        # -----------------------------
        # Markdown destination
        # -----------------------------
        output_md = markdown_output_path(
            repo_path,
            department,
            semester,
            subject,
            unit,
        )

        # -----------------------------
        # Convert to Markdown
        # -----------------------------
        convert_to_markdown(
            pdf_path,
            output_md,
        )

        # -----------------------------
        # Update index.json
        # -----------------------------
        save_index(repo_path)

        # -----------------------------
        # Commit
        # -----------------------------
        commit_changes(
            repo_path,
            f"Added {department} {semester} {subject} {unit}",
        )

        # -----------------------------
        # Push
        # -----------------------------
        push_changes(repo_path)

        return output_md

    finally:

        # -----------------------------
        # Delete uploaded PDF
        # -----------------------------
        if pdf_path and pdf_path.exists():
            pdf_path.unlink()

        # -----------------------------
        # Delete temporary repository
        # -----------------------------
        if repo_path:
            cleanup_repository(repo_path)