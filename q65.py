# Q65) Problem statement: Accept a list of numbers and display the largest and
# smallest values using max() and min().

numbers = [int(x) for x in input("Enter numbers (space separated): ").split()]
print(f"Maximum: {max(numbers)}; Minimum: {min(numbers)}")
