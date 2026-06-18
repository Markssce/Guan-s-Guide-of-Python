# List comprehension

# String -> Float
str_nums = ["1.2", "3.5", "9.0", "-2.1"]
float_nums = [float(x) for x in str_nums]
# print(float_nums)

# count/index
lst = [2, 4, 5, 3, 2, 9]
res = [x for x in lst if lst.count(x) > 1]
print(res)