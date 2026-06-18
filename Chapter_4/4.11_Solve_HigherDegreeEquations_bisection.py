import math
# Function of concentration

def fx(x):
    global concentration # 使用全局变量
    ka = 10**(-4.56) #醋酸的 ka
    kw = 1e-14
    kakw = ka*kw
    f = x**3 + ka*x**2 - (ka*concentration + kw)*x - kakw
    return f

# Find zero point

def biAlgorithm(a, b, func):
    fa = func(a)
    while (abs(a-b) > 1e-10):
        m = (a+b)/2
        fm = func(m)
        if (fa*fm > 0):
            a = m
        else:
            b = m
    return a

fa = 1
fb = 1
concentration = float(input("Enter the concentration of acetic acid"))
while (fa * fb > 0):
    # Interval
    a = float(input("Enter the left interval"))
    b = float(input("Enter the right interval"))
    fa = fx(a)
    fb = fx(b)
ans = biAlgorithm(a, b, fx)
pH = -math.log10(ans)
print(pH)