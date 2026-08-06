import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DEFAULT_REPOSITORY = Path(r"C:\repositories\college-materials")

REPOSITORY = Path(
    os.getenv(
        "COLLEGE_REPOSITORY",
        str(DEFAULT_REPOSITORY)
    )
)

GITHUB_OWNER = "Mounikaishu"
GITHUB_REPO = "college-materials"
GITHUB_BRANCH = "main"

UPLOAD_FOLDER = BASE_DIR / "uploads"
TEMP_FOLDER = BASE_DIR / "temp"

UPLOAD_FOLDER.mkdir(exist_ok=True)
TEMP_FOLDER.mkdir(exist_ok=True)