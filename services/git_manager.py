import shutil
import subprocess
import uuid
import time
from pathlib import Path

from config import (
    TEMP_FOLDER,
    GITHUB_REPO_URL,
    GITHUB_BRANCH,
)

# -----------------------------
# Clone Repository
# -----------------------------
def clone_repository():

    repo_path = TEMP_FOLDER / f"repo_{uuid.uuid4().hex}"

    subprocess.run(
        [
            "git",
            "clone",
            GITHUB_REPO_URL,
            str(repo_path),
        ],
        check=True,
    )

    # Configure Git identity for this temporary repository
    subprocess.run(
        [
            "git",
            "config",
            "user.name",
            "LMS Bot",
        ],
        cwd=repo_path,
        check=True,
    )

    subprocess.run(
        [
            "git",
            "config",
            "user.email",
            "lms@example.com",
        ],
        cwd=repo_path,
        check=True,
    )

    return repo_path


# -----------------------------
# Commit
# -----------------------------
def commit_changes(repo_path, message):

    subprocess.run(
        ["git", "add", "."],
        cwd=repo_path,
        check=True,
    )

    # Only commit if there are changes
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=repo_path,
        capture_output=True,
        text=True,
        check=True,
    )

    if result.stdout.strip():

        subprocess.run(
            [
                "git",
                "commit",
                "-m",
                message,
            ],
            cwd=repo_path,
            check=True,
        )


# -----------------------------
# Push
# -----------------------------
def push_changes(repo_path):

    subprocess.run(
        [
            "git",
            "push",
            "origin",
            GITHUB_BRANCH,
        ],
        cwd=repo_path,
        check=True,
    )


# -----------------------------
# Cleanup
# -----------------------------
def cleanup_repository(repo_path):

    repo_path = Path(repo_path)

    for _ in range(5):

        try:
            shutil.rmtree(repo_path)
            return

        except PermissionError:
            time.sleep(1)

    print(f"Warning: Could not delete {repo_path}")