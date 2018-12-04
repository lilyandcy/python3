class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        res = []
        wordList = A.split(" ") + B.split(" ")
        for word in wordList:
            if wordList.count(word) < 2:
                res.append(word)
        return res
