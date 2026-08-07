from services.git_manager import (
    clone_repository,
    commit_changes,
    push_changes,
    cleanup_repository,
)

from services.index_service import save_index
from services.converter import convert_to_markdown
from config import UPLOAD_FOLDER


def sanitize_name(name):
    return (
        name.strip()
            .replace(" ", "_")
            .replace("/", "-")
            .replace("\\", "-")
    )


def save_uploaded_file(uploaded_file):

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

    folder = (
    repo_path
    / sanitize_name(department)
    / sanitize_name(semester)
    / sanitize_name(subject)
)

    folder.mkdir(
        parents=True,
        exist_ok=True,
    )

    safe_unit = sanitize_name(unit)

    return folder / f"{safe_unit}.md"


def process_upload(
    uploaded_file,
    department,
    semester,
    subject,
    unit,
):

    repo = None
    pdf_path = None

    try:

        # Save uploaded file
        pdf_path = save_uploaded_file(uploaded_file)

        # Clone repository
        repo = clone_repository()

        # Create markdown destination inside cloned repo
        output_md = markdown_output_path(
            repo,
            department,
            semester,
            subject,
            unit,
        )

        # Convert PDF -> Markdown
        convert_to_markdown(
            pdf_path,
            output_md,
        )

        # Update index.json inside cloned repo
        save_index(repo)

        # Commit
        commit_changes(
            repo,
            f"Added {department} {semester} {subject} {unit}",
        )

        # Push
        push_changes(repo)

        return output_md

    finally:

        if pdf_path and pdf_path.exists():
            pdf_path.unlink()

        if repo:
            cleanup_repository(repo)