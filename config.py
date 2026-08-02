from pathlib import Path

# ==========================
# Project Root
# ==========================
BASE_DIR = Path(__file__).resolve().parent

# ==========================
# Repository
# ==========================
REPOSITORY = BASE_DIR / "repositories" / "college-materials"

# ==========================
# Upload Folder
# ==========================
UPLOAD_FOLDER = BASE_DIR / "uploads"

# ==========================
# Temporary Folder
# ==========================
TEMP_FOLDER = BASE_DIR / "temp"

# ==========================
# Create folders if missing
# ==========================
UPLOAD_FOLDER.mkdir(exist_ok=True)
TEMP_FOLDER.mkdir(exist_ok=True)