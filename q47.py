# Q47) Problem statement: Accept a positive integer n and calculate the sum of
# all even numbers from 1 to n.

# Accept a positive integer (n) and calculate the sum of all even numbers from 1 to (n).


n = int(input("Enter a positive integer: "))
total = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        total += i
print(total)
