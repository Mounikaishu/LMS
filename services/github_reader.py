import requests

from config import (
    GITHUB_OWNER,
    GITHUB_REPO,
    GITHUB_BRANCH
)


BASE_RAW_URL = (
    f"https://raw.githubusercontent.com/"
    f"{GITHUB_OWNER}/"
    f"{GITHUB_REPO}/"
    f"{GITHUB_BRANCH}"
)


def get_markdown(
    department,
    semester,
    subject,
    unit
):
    url = (
        f"{BASE_RAW_URL}/"
        f"{department}/"
        f"{semester}/"
        f"{subject}/"
        f"{unit}.md"
    )

    print("Markdown URL:", url)

    response = requests.get(url)

    print("Status Code:", response.status_code)

    if response.status_code != 200:
        return None

    return response.text