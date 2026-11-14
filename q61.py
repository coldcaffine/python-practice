# Q61) Problem statement: Create a dictionary of three fruits and their prices.
# Use items() to display each fruit and its corresponding price.

fruits = {"Apple": 100, "Mango": 80, "Banana": 40}
for fruit, price in fruits.items():
    print(f"{fruit}: {price}")
