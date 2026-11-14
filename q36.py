# Q36) Problem statement: Create a dictionary of student names and marks.
# Retrieve a student's marks using get(). If the student is absent, display a
# default message.

# Create a dictionary of student names and marks. Retrieve a student's marks using get(). If the student is absent, display a default message.


students = {"Asha": 85, "Ravi": 75, "Amit": 90}
name = input("Enter student name: ")
print(students.get(name, "Student not found"))
