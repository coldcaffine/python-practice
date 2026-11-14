# Q59) Problem statement: Create a dictionary of student details and display all
# keys using keys() and all values using values().

student = {"name": "Asha", "marks": 80}
print("Keys:", ", ".join(student.keys()))
print("Values:", ", ".join(str(v) for v in student.values()))
