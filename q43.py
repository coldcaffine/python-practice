# Q43) Problem statement: Accept a number and display its multiplication table
# from 1 to 10 using a for loop.

# Accept a number and display its multiplication table from 1 to 10 using a for loop.


n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
