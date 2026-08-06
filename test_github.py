from services.github_reader import get_markdown

content = get_markdown(
    "IT",
    "Semester1",
    "DBMS",
    "1"
)

print(content)