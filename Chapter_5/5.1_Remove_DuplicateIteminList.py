# Given a list containing duplicate elements, write a program to remove duplicates and generate a new list.

L = [1, 3, 4, 5, 5, 1]

# Ans1: set
# L1 = list(set(L))
# print(L1)

# Ans2:  traverse
newL = []
for i in L:
    if not i in newL:
        newL += [i]
print(newL)