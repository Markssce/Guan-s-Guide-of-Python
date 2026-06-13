# Find the greatest common divisor of two natural numbers.

m, n = eval(input("Enter m, n:"))
# Brute-force method
min_ = min(m,n)
while not (m % min_ == 0 and n % min_ == 0):
    min_ = min_-1
print("The greatest common divisor is {}".format(min_))# Euclidean algorithm
# Euclidean algorithm
if m > n:
    m,n = n,m
r = m%n
while r != 0:
    m = n
    n = r
    r = m%n
print("The greatest common divisor is {}".format(n))