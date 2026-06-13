# Based on this growth rate(0.00381), calculate in how many years will the national population double.

import math
populaiton_ = 13.95
growth_rate = 0.00381
flag = 0
while populaiton_ < 27.9:
    flag += 1
    populaiton_ = populaiton_*(1 + growth_rate)
print("There will be {} years, and the population is {}".format(flag, populaiton_))
