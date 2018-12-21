class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        orderMap = {}
        for i in range(len(order)):
            orderMap[order[i]] = i
        orderMap[" "] = -1
        for j in range(20):
            compareWord = []
            for i in range(len(words)):
                if j >= len(words[i]):
                    compareWord.append(" ")
                else:
                    compareWord.append(words[i][j])
            if compareWord.count(compareWord[0]) == 1:
                return self.isSorted(compareWord, orderMap)
            else:
                if self.isSorted(compareWord, orderMap) == False:
                    return False

    def isSorted(self, words, orderMap):
        for i in range(len(words)-1):
            if orderMap[words[i]] > orderMap[words[i+1]]:
                return False
        return True