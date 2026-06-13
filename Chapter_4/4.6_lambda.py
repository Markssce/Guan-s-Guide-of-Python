# Calculate the mean and the standard error of a given list with lambda fuction.

import math

aver = lambda L: sum(L)/len(L)
sigma = lambda L,aver: math.sqrt(sum([(i-aver)**2 for i in L])/(len(L)-1))
list_ = [1, 2, 100, 45]
average_ = aver(list_)
print(sigma(list_, average_))