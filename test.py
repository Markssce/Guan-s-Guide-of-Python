import mlx.core as mx
a = mx.array([1, 2, 3, 4])
b = mx.array([1.0, 2.0, 3.0 ,4.0])
c = a + b
mx.eval(c)
print(c)