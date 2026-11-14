# Q46) Problem statement: Accept a tuple and a target value. Use index() to
# display the index of the first occurrence of the target.

# Accept a tuple and a target value. Use index() to display the index of the first occurrence of the target.


t = tuple(input("Enter tuple elements (space separated): ").split())
target = input("Enter target value: ")

if target in t:
    print(f"Index: {t.index(target)}")
else:
    print("Target not found")
