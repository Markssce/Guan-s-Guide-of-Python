# Store the three coefficients of the quadratic equation with one variable in a sequence, and call the function to solve the equation by unpacking the actual parameters.

# import math
# def solve_quadricEquation(a, b, c):
#     delta = b**2 - 4*a*c
#     if delta > 0:
#         root_1 = (-b+math.sqrt(b**2 - 4*a*c)) / (2*a)
#         root_2 = (-b-math.sqrt(b**2 - 4*a*c)) / (2*a)
#         print("Roots are{0:5.2f} and {1:5.2f}.".format(root_1, root_2))
#         return [root_1, root_2]

#     else:
#         print("There's no root.")
#         return []

# L = [2, 7, -3]
# solve_quadricEquation(*L)

# Implement matrix transposition by unpacking actual parameters.

X = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
Xt = list(map(list, zip(*X)))
print(Xt)