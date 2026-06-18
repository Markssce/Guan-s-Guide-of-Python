# The index method can be used in combination with the count method.

lst = [2, 5, 3, 2, 9, 2, 7]
target = 3

total = lst.count(target)
first_pos = lst.index(target)

print(f"Num{target} appears {total} times")
print(f"Num{target} first appears at {first_pos}")