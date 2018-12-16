class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        factor = []
        if num == 1:
            return False
        for i in range(1, num//2 + 1):
            if num % i == 0:
                factor.append(i)
        if sum(factor) == num:
            return True
        else:
            return False