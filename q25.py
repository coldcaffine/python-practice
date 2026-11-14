# Q25) Problem statement: Accept two numbers and display the larger number. If
# both are equal, display an appropriate message.

#  Accept two numbers and display the larger number. If both are equal, display an appropriate message.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print(f"Largest = {a:g}")
elif b > a:
    print(f"Largest = {b:g}")
else:
    print("Both numbers are equal")
