# Q17) Problem statement: Accept two integers and display the quotient and
# remainder when the first integer is divided by the second. Assume the divisor
# is nonzero.

# Accept two integers and display the quotient and remainder when the first integer is divided by the second. Assume the divisor is nonzero.

a = int(input("Enter dividend: "))
b = int(input("Enter divisor (nonzero): "))

print(f'Quotient = {a // b}: Remainder = {a % b}')
