class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        strnum =""
        count = 0
        for i in range(1, N+1):
            strnum = str(i)
            if strnum.count("3") == 0 and strnum.count("4") == 0 and strnum.count("7") == 0:
                if strnum.count("0") + strnum.count("1") + strnum.count("8") != len(strnum):
                    count = count + 1
        return count