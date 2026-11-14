# Q51) Problem statement: Create a dictionary containing a student's name, roll
# number, and department. Display all key-value pairs.

# Create a dictionary containing a student's name, roll number, and department. Display all key-value pairs.

student = {"name": "Asha", "roll": 101, "department": "CSBS"}
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")
