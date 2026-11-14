# Q15) Problem statement: Accept principal, rate of interest, and time.
# Calculate simple interest using the formula SI=(P*R*T)/100.

#  Accept principal, rate of interest, and time. Calculate simple interest using the formula  SI=(P*R*T)/100

p = float(input("Enter Principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100
print(f"Interest = {si:g}")
