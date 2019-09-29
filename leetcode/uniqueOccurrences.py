class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrDict = {}
        for key in arr:
            if key not in arrDict:
                arrDict[key] = 1
            else:
                arrDict[key] += 1
        valueList = []
        for key in arrDict:
            valueList.append(arrDict[key])
        return len(valueList) == len(set(valueList))