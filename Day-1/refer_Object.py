x = [1, 2, 3, 4]
y = x
y[0] = 5
print(x)
print(y)

x = [1, 2, 3, 4]
z = x.copy()
z[0] = 5
print(x)
print(z)