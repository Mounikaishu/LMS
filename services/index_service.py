import json
from pathlib import Path


from pathlib import Path
import json

import json
from pathlib import Path


VALID_DEPARTMENTS = {
    "IT",
    "CSE",
    "ECE",
    "AI-DS"
}


def build_index(repository):
    repository = Path(repository)

    data = {}

    for department in repository.iterdir():

        # Skip files
        if not department.is_dir():
            continue

        # Skip hidden/system folders (.git, .github, etc.)
        if department.name.startswith("."):
            continue

        # Only scan valid departments
        if department.name not in VALID_DEPARTMENTS:
            continue
        if department.name.startswith("."):
            continue

        dept = {}

        for semester in department.iterdir():

            if not semester.is_dir():
                continue

            sem = {}

            for subject in semester.iterdir():

                if not subject.is_dir():
                    continue

                units = []

                for md in subject.glob("*.md"):
                    units.append(md.stem)

                # Sort numerically if possible
                try:
                    units = sorted(units, key=int)
                except ValueError:
                    units = sorted(units)

                sem[subject.name] = units

            dept[semester.name] = sem

        data[department.name] = dept

    return data


def save_index(repository):
    repository = Path(repository)

    data = build_index(repository)

    index_file = repository / "index.json"

    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )
def save_index(
    repository
):

    repository = Path(repository)

    data = build_index(repository)

    file = repository / "index.json"

    with open(
        file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )
def save_index(repository):
    repository = Path(repository)

    print("Saving index from:", repository)

    data = build_index(repository)

    print("Generated data:")
    print(json.dumps(data, indent=4))

    file = repository / "index.json"

    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        