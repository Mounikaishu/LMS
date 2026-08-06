import requests

from config import (
    GITHUB_OWNER,
    GITHUB_REPO,
    GITHUB_BRANCH,
)

INDEX_URL = (
    f"https://raw.githubusercontent.com/"
    f"{GITHUB_OWNER}/"
    f"{GITHUB_REPO}/"
    f"{GITHUB_BRANCH}/index.json"
)


def load_index():
    response = requests.get(
        INDEX_URL,
        headers={"Cache-Control": "no-cache"}
    )

    if response.status_code != 200:
        return {}

    return response.json()

    if response.status_code != 200:
        return {}

    return response.json()


def get_departments(data):
    return sorted(
        dept
        for dept in data.keys()
        if not dept.startswith(".")
    )


def get_semesters(data, department):
    return sorted(
        data.get(department, {}).keys()
    )


def get_subjects(data, department, semester):
    return sorted(
        data.get(department, {})
            .get(semester, {})
            .keys()
    )


def get_units(data, department, semester, subject):
    units = (
        data.get(department, {})
            .get(semester, {})
            .get(subject, [])
    )

    # If all units are numeric, sort numerically
    if all(unit.isdigit() for unit in units):
        return sorted(units, key=int)

    # Otherwise sort alphabetically
    return sorted(units)