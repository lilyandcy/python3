sumup = 0
sumupEven = 0

for i in range(1, 1001) :
    sumup = sumup + i
print(sumup)

for i in range(1, 1001) :
    if i%2 == 0 :
        sumupEven = sumupEven + i
print(sumupEven)