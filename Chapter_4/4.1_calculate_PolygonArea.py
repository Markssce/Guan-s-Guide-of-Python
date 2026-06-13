# Calculate the area of pentagon with all sides and diagonals.

import math
def cal_area_triangle(x, y, z):
    c = 0.5*(x+y+z)
    area = math.sqrt(c*(c-x)*(c-y)*(c-z))
    return area

a, b, c, d, e, f, g = eval(input("Enter all sides and daigonals of the pentagon: "))
Ans_area = cal_area_triangle(a, b, c) + cal_area_triangle(c, e, d) + cal_area_triangle(g, f, e)
print(Ans_area)