import math

# Solve the roots of a quadratic equation
# Enter the coefficients
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
delta = b*b - 4*a*c
if delta >= 0:
    root_1 = (-b + math.sqrt(delta))/(2*a)
    root_2 = (-b - math.sqrt(delta))/(2*a)
    print("Roots are %8.4f and %8.4f. "%(root_1, root_2))
else:
    print("There is no root. ")