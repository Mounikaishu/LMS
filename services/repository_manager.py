from pathlib import Path
from config import REPOSITORY


def get_departments():
    return [
        "IT",
        "CSE",
        "ECE",
        "AI-DS"
    ]


def get_semesters():
    return [
        "Semester1",
        "Semester2",
        "Semester3",
        "Semester4",
        "Semester5",
        "Semester6",
        "Semester7",
        "Semester8",
    ]


def get_subjects(department, semester):

    path = REPOSITORY / department / semester

    if not path.exists():
        return []

    return sorted(
        [
            folder.name
            for folder in path.iterdir()
            if folder.is_dir() and not folder.name.startswith(".")
        ]
    )


def get_units(department, semester, subject):

    path = REPOSITORY / department / semester / subject

    if not path.exists():
        return []

    return sorted(
        [
            file.stem
            for file in path.glob("*.md")
        ]
    )


def create_subject(department, semester, subject):

    path = REPOSITORY / department / semester / subject

    path.mkdir(parents=True, exist_ok=True)

    return path


def create_unit(department, semester, subject, unit):

    path = REPOSITORY / department / semester / subject

    path.mkdir(parents=True, exist_ok=True)

    return path / f"{unit}.md"