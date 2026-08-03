from pathlib import Path
from config import REPOSITORY


def get_departments():

    departments = []

    for folder in REPOSITORY.iterdir():

        # Ignore hidden folders like .git
        if folder.name.startswith("."):
            continue

        if folder.is_dir():
            departments.append(folder.name)

    return sorted(departments)

def get_semesters(department):

    path = REPOSITORY / department

    if not path.exists():
        return []

    semesters = []

    for folder in path.iterdir():

        if folder.name.startswith("."):
            continue

        if folder.is_dir():
            semesters.append(folder.name)

    return sorted(semesters)


def get_subjects(department, semester):

    path = REPOSITORY / department / semester

    if not path.exists():
        return []

    subjects = []

    for folder in path.iterdir():

        if folder.name.startswith("."):
            continue

        if folder.is_dir():
            subjects.append(folder.name)

    return sorted(subjects)


def get_units(department, semester, subject):

    path = REPOSITORY / department / semester / subject

    if not path.exists():
        return []

    units = []

    for file in path.glob("*.md"):
        units.append(file.stem)

    return sorted(units)


def load_markdown(
    department,
    semester,
    subject,
    unit
):

    file = (
        REPOSITORY
        / department
        / semester
        / subject
        / f"{unit}.md"
    )

    if not file.exists():
        return None

    return file.read_text(encoding="utf-8")