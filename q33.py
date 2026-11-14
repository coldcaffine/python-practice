# Q33) Problem statement: Accept two numbers and an operator (+, -, *, or /).
# Use conditional statements to perform the selected calculation.

# Accept two numbers and an operator (+, -, *, or /). Use conditional statements to perform the selected calculation.


a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if op == "+":
    print(f"{a + b:g}")
elif op == "-":
    print(f"{a - b:g}")
elif op == "*":
    print(f"{a * b:g}")
elif op == "/":
    if b != 0:
        print(f"{a / b:g}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
