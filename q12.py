# Q12) Problem statement: Define a function named square() that accepts a number
# and returns its square.

# define a function named square() that accepts a number and returns its square.

def square(n):
    return n * n


num = float(input("Enter a number: "))
print(f"{square(num):g}")
