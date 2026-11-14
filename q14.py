# Q14) Problem statement: Define a function that accepts a non-negative integer
# and returns its factorial. Call the function for the given inputs.

# function that accepts a non-negative integer and returns its factorial. Call the function for the given inputs

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n = int(input("Enter a non negative integer: "))
print(factorial(n))
