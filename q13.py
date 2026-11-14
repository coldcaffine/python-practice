# Q13) Problem statement: Write a Python program to swap the values of two
# variables using a temporary variable.

# Write a Python program to swap the values of two variables using a temporary variable.
a = int(input("Enter A: "))
b = int(input("Enter B: "))

temp = a
b = a
a = temp

print(f"A = {a}, B = {b}")
