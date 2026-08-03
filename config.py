from pathlib import Path
import os

# ==============================
# LMS Project Directory
# ==============================

BASE_DIR = Path(__file__).resolve().parent

# ==============================
# Repository Path
# ==============================

DEFAULT_REPOSITORY = Path(r"C:\repositories\college-materials")


REPOSITORY = Path(
    os.getenv(
        "COLLEGE_REPOSITORY",
        str(DEFAULT_REPOSITORY)
    )
)

# ==============================
# Local Folders
# ==============================

UPLOAD_FOLDER = BASE_DIR / "uploads"
TEMP_FOLDER = BASE_DIR / "temp"

UPLOAD_FOLDER.mkdir(exist_ok=True)
TEMP_FOLDER.mkdir(exist_ok=True)
print("Repository Path:", REPOSITORY)