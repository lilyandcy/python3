class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mapWords = {}
        res = []
        tempres =[]
        for word in words:
            if word in mapWords.keys():
                mapWords[word] += 1
            else:
                mapWords[word] = 1
        listWords = sorted(mapWords.items(), key = lambda x:x[1], reverse = True)
        curValue = listWords[0][1]
        for i in range(len(listWords)):
            if listWords[i][1] != curValue:
                curValue = listWords[i][1]
                res += sorted(tempres)
                tempres = []
                tempres.append(listWords[i][0])
            else:
                tempres.append(listWords[i][0])
        res += sorted(tempres)
        return res[:k]