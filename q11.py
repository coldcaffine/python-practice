# Q11) Problem statement: Write a Python program to accept a temperature in
# Celsius and convert it into Fahrenheit using the formula F=(C*9/5+32).

# Write a Python program to accept a temperature in Celsius and convert it into Fahrenheit using the formula F=(C*9/5+32 )

c = float(input("Enter temperature in Celcius: "))
f = (c * 9 / 5) + 32
print(f"{f:g} Fahrenheit")
