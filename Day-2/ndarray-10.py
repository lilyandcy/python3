import numpy as np

a = np.arange(5)
print(a)
b = a[2:].copy()
print(b)
b[0] = 100
print(b)
print(a)