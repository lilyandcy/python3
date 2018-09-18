class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if 0 <= num < 10:
            return num
        else:
            sumnum = 0
            for i in range(len(str(num))):
                sumnum = sumnum + int(str(num)[i])
            return self.addDigits(sumnum)