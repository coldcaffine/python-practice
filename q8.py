# Q8) Problem statement: Create a global variable and a function containing a
# local variable. Display both variables to demonstrate the difference between
# global and local scope.

# Create a global variable and a function containing a local variable. Display both variables to demonstrate the difference between global and local scope.

global_var = 10


def show():
    local_var = 5
    print("Local:", local_var)


print("Global:", global_var)
show()
