# Q45) Problem statement: Accept a non-negative integer and calculate its
# factorial using a while loop.

# Accept a non-negative integer and calculate its factorial using a while loop.


n = int(input("Enter a non-negative integer: "))

result = 1
i = n
while i > 1:
    result *= i
    i -= 1

print(result)
