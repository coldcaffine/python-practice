# Q10) Problem statement: Define a function named greet() that accepts a
# person's name and a greeting message. Use a default greeting when no message
# is provided.

#  Define a function named greet() that accepts a person's name and a greeting message. Use a default greeting when no message is provided.

def greet(name, message="Hello"):
    print(f"{message}, {name}!")


greet("Asha")
greet("Ravi", "Welcome")
greet("Neha")
