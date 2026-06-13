# Generate 10 numbers with sample() and calculate the max, min and mean.

import random
list_ = random.sample(range(1,101),10)
print(list_)
min_ = 100
max_ = 0
sum_ = 0
for i in list_:
    if i > max_:
        max_ = i
    if i < min_:
        min_ = i
    sum_ += i
print("max={}, min={}, mean={}".format(max_,min_,sum_/10))