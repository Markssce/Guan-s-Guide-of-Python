import random

# Generate 10 uppercase letters randomly.
list_res = []
# random.seed(1) # Fix the seed so that the answer ain't change
for i in range(10):
    list_res.append(chr((random.randint(65,90))))
print(list_res)

# Brief Ans
print([].append(chr((random.randint(65,90)))) for i in range(10))