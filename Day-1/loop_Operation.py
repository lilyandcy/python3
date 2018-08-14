# example of for and range
# default start of range is 0
# default step of range is 1
l = []
for i in range(2, 10, 3) :
    print(i)
    l.append(i**2)
print(l)

# while to sum up 1 to 100
a = 0
sumup = 0
while a < 100 :
    a = a + 1
    sumup = sumup + a
print(sumup)