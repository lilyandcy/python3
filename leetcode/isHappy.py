class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        looplist = []
        num = n
        while num != 1:
            if num not in looplist:
                looplist.append(num)
            else:
                return False
            num = self.sumLocation(num)
        return True

    def sumLocation(self, num):
        strnum = str(num)
        sumnum = 0
        for i in range(len(strnum)):
            sumnum += int(strnum[i]) ** 2
        return sumnum