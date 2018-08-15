import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = a.copy()

c1 = np.dot(np.transpose(a), b)
print(c1)
c2 = np.dot(a, np.transpose(b))
print(c2)

ax = np.reshape(a, (5, 1))
bx = np.reshape(b, (1, 5))
c = np.dot(ax, bx)
print(c)