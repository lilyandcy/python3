def calcFunc(x = 1) :
    y = x ** (x/3)
    return (y)
startX = 1
appResult = calcFunc(startX)
while (appResult - 2 >=0.000001) or (2 - appResult >= 0.000001) :
    if appResult - 2 <=0 :
        startX = startX + 0.0000001
    else :
        startX = startX - 0.0000001
    appResult = calcFunc(startX)

print(startX)