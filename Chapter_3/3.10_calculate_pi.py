# Calculate pi with Gregory's formula

pi_q = 0
sign = n = 1
while abs(abs(sign / n)) > 1e-6:
    pi_q = pi_q + 1/n
    n = -sign * (abs(n)+2)
    sign = -sign
print(pi_q*4)