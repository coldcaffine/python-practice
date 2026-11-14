# Q63) Problem statement: Accept a list of numbers and calculate the total using
# the built-in sum() function.

numbers = [int(x) for x in input("Enter numbers (space separated): ").split()]
print(f"Sum: {sum(numbers)}")
