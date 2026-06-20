def Fibs(n):
    a, b = 0, 1
    while a < n:
        value = a
        a, b = b, a+b
        yield value 
for item in Fibs(10):
    print(item, end = " ")

# Generator expression
# square_gen = (x*x for x in range(1,10)) 
# for i in square_gen:
# 	print(i)