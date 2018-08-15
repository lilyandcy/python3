import numpy as np

a = np.arange(12)
a = a.reshape(3, 4)
print(a)

print(a[:,1])
print(a[2,:])
print(a[1][2])
print(a[2])