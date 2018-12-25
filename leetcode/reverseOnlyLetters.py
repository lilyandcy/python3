class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S) < 2:
            return S
        else:
            tempList = []
            for i in range(len(S)):
                tempList.append(S[i])
            revS = S[::-1]
            rtempList = []
            for i in range(len(revS)):
                if revS[i].isalpha():
                    rtempList.append(revS[i])
            j = 0
            i = 0
            while i < len(rtempList):
                if tempList[j].isalpha():
                    tempList[j] = rtempList[i]
                    j += 1
                    i += 1
                else:
                    j += 1
            res = ""
            return res.join(tempList)