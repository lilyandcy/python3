import numpy as np

a = np.linspace(0, 1, 12)
a = a.reshape(3, 4)
print (a)
np.savetxt('../res/myfile.txt', a)
np.save('../res/myfile', a)

b = np.loadtxt('../res/myfile.txt')
c = np.load('../res/myfile.npy')

print(b)
print(c)