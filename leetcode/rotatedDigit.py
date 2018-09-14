class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        goodset = {"2", "5", "6", "9"}
        ucset = {"0", "1", "8"}
        badset = {"3", "4", "7"}
        goodcount = 0
        for i in range(1, N+1):
            setNum = set(list(str(i)))
            if len(setNum) == 1:
                if setNum.issubset(goodset):
                    goodcount = goodcount + 1
            else:
                if setNum.issubset(goodset|ucset) and (setNum & goodset):
                    goodcount = goodcount + 1
        return goodcount