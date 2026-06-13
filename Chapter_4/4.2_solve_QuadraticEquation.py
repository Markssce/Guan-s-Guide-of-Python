# Write a function quadricEquation(a, b, c) to calculate the real roots of a quadratic equation with one variable, then call this function to solve the roots of 2x^2+7x-3=0.

import math
def solve_quadricEquation(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        root_1 = (-b+math.sqrt(b**2 - 4*a*c)) / (2*a)
        root_2 = (-b-math.sqrt(b**2 - 4*a*c)) / (2*a)
        print("Roots are{0:5.2f} and {1:5.2f}.".format(root_1, root_2))
        return [root_1, root_2]

    else:
        print("There's no root.")
        return []

solve_quadricEquation(2, 7, -3)