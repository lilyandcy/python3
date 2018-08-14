def selectSort(inputList) :
    inputListLen = len(inputList)
    outputList = []
    while inputListLen > 0 :
        maxE= 0
        for e in inputList :
            if e >= maxE :
                maxE = e
                index = inputList.index(e)
            else :
                continue
        outputList.append(maxE)
        del inputList[index]
        inputListLen = len(inputList)
    return (outputList)

def bubbleSort(inputList) :
    inputListLen = len(inputList)
    j = 0
    while j < inputListLen :
        for i in range(inputListLen-1) :
            temp = inputList[i]
            if inputList[i] < inputList[i+1] :
                inputList[i] = inputList[i+1]
                inputList[i+1] = temp
        j = j + 1
    return (inputList)

def insertSort(inputList) :
    inputListLen = len(inputList)
    for j in range(inputListLen) :
        for i in range(j+1, inputListLen) :
            temp = inputList[j]
            if inputList[i] >= inputList[j] :
                inputList[j] = inputList[i]
                inputList[i] = temp
    return(inputList)




unsortedList = [8, 2, 4, 6, 1, 0, 9, 3, 5, 7]
sortedList = insertSort(unsortedList)
print(sortedList)