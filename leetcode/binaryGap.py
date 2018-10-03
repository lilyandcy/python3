class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binN = bin(N)
        strN = str(binN)[2:]
        if strN.count("1") < 2:
            return 0
        maxd = 0
        startIndex = strN.find("1")
        s = startIndex + 1
        for i in range(s, len(strN)):
            if strN[i] == "1":
                distance = i - startIndex
                startIndex = i
                if maxd < distance:
                    maxd = distance
        return maxd
