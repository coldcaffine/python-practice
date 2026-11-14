# Q70) Problem statement: Accept a list and a number. Use count() to calculate
# how many times the number occurs.

numbers = [int(x) for x in input("Enter numbers (space separated): ").split()]
target = int(input("Enter number to count: "))
print(f"Count: {numbers.count(target)}")
