from pathlib import Path

# -----------------------------
# Base Directories
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent

UPLOAD_FOLDER = BASE_DIR / "uploads"
TEMP_FOLDER = BASE_DIR / "temp"

UPLOAD_FOLDER.mkdir(exist_ok=True)
TEMP_FOLDER.mkdir(exist_ok=True)

# -----------------------------
# GitHub Configuration
# -----------------------------

GITHUB_OWNER = "Mounikaishu"
GITHUB_REPO = "college-materials"
GITHUB_BRANCH = "main"

GITHUB_REPO_URL = (
    f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}.git"
)