from pathlib import Path
import subprocess


def push_changes(repo_path: Path, message: str):

    subprocess.run(
        ["git", "-C", str(repo_path), "add", "."],
        check=True
    )

    subprocess.run(
        [
            "git",
            "-C",
            str(repo_path),
            "commit",
            "-m",
            message
        ],
        check=True
    )

    subprocess.run(
        [
            "git",
            "-C",
            str(repo_path),
            "push",
            "origin",
            "main"
        ],
        check=True
    )