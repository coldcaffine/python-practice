# Q5) Problem statement: Write a Python program to accept two numbers and
# perform addition, subtraction, multiplication, and division.

# Write a Python program to accept two numbers and perform addition, subtraction, multiplication, and division.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print(f"Addition: {a + b:g}")
print(f"Subtraction: {a - b:g}")
print(f"Multiplication: {a * b:g}")
if b != 0:
    print(f"Divison: {a / b:g}")
else:
    print("Divison cannot divide by zero")
