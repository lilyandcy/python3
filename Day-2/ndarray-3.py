import numpy as np

a1 = np.array([[1, 2, 3], [4, 5, 6]])
print(a1)
print(a1.shape)
print(a1.ndim)
print(a1.size)

a = np.arange(0, 20, 1)
b = a.reshape((4, 5))
c = a.reshape((10, 2))
d = a.reshape((-1, 4))

print(a)
print(b)
print(c)
print(d)