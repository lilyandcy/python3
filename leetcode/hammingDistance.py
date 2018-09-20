class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        c = x ^ y
        binc = bin(c)
        strtemp = str(binc)
        strc = strtemp[2:]
        distance = 0
        for i in range(len(strc)):
            if strc[i] == "1":
                distance += 1
        return distance