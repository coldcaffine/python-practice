# Q41) Problem statement: Accept a positive integer n and calculate the sum of
# numbers from 1 to n using a loop.

#  Accept a positive integer (n) and calculate the sum of numbers from 1 to (n) using a loop.


n = int(input("Enter a positive integer: "))
total = 0
for i in range(1, n + 1):
    total += i
print(total)
