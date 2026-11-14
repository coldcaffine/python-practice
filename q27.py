# Q27) Problem statement: Accept a person's age and check whether the person is
# eligible to vote. Consider 18 years as the minimum age.

# Accept a person's age and check whether the person is eligible to vote. Consider 18 years as the minimum age.


age = int(input("Enter age: "))
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
