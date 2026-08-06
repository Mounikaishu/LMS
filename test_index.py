from services.github_index_reader import *

print(get_departments())
print(get_semesters("IT"))
print(get_subjects("IT", "Semester1"))
print(get_units("IT", "Semester1", "DBMS"))