# Q49) Problem statement: Accept a non-negative integer and count the number of
# digits using a while loop.

# Accept a non-negative integer and count the number of digits using a while loop.

n = int(input("Enter a non-negative integer: "))

if n == 0:
    count = 1
else:
    count = 0
    while n > 0:
        n //= 10
        count += 1

print(f"{count} digit" if count == 1 else f"{count} digits")
