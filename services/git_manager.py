import subprocess
from config import REPOSITORY


def git_push(commit_message):

    subprocess.run(
        ["git", "add", "."],
        cwd=REPOSITORY,
        check=True
    )

    subprocess.run(
        ["git", "commit", "-m", commit_message],
        cwd=REPOSITORY,
        check=True
    )

    subprocess.run(
        ["git", "push", "origin", "main"],
        cwd=REPOSITORY,
        check=True
    )