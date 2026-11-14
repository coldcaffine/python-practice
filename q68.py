# Q68) Problem statement: Accept a list of numbers and arrange the elements in
# ascending order using sort().

numbers = [int(x) for x in input("Enter numbers (space separated): ").split()]
numbers.sort()
print(numbers)
