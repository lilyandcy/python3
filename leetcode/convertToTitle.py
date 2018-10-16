class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        dictList = ["Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        while n > 26:
            res = dictList[n % 26] + res
            if n % 26 == 0:
                n = n // 26 - 1
            else:
                n = n // 26
        res = dictList[n] + res
        return res