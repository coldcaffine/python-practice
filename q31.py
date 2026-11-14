# Q31) Problem statement: Accept a student's percentage and assign a grade using
# if-elif-else: A for 80 and above, B for 60-79, C for 40-59, and F below 40.

# Accept a student's percentage and assign a grade using if-elif-else: A for 80 and above, B for 60–79, C for 40–59, and F below 40

percent = float(input("Enter percentage: "))

if percent >= 80:
    print("Grade A")
elif percent >= 60:
    print("Grade B")
elif percent >= 40:
    print("Grade C")
else:
    print("Grade F")
