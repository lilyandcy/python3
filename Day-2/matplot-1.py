import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 201)
plt.figure(figsize=(4, 4))
plt.plot(x, x**0.5, 'r--')
plt.plot(x, x-1, 'k-')
plt.plot(x, np.zeros_like(x), 'k-')
plt.show()
