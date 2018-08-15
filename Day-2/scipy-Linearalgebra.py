import numpy as np
from scipy import linalg

A = np.random.randn(5, 5)
b = np.random.randn(5)
x = linalg.solve(A, b) # Solve A x = b
#print(x)
eigen = linalg.eig(A)
#print(eigen)
det = linalg.det(A)
print(det)