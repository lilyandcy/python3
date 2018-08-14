def fabnacciN(n=1):
    fList=[1, 1]
    if n == 1 :
        return fList[0]
    if n == 2 :
        return fList[1]
    if n > 2 :
        for i in range(2, n) :
            fList.append(fList[i-2]+fList[i-1])
    return fList[n-1]

result = fabnacciN(2)
print(result)