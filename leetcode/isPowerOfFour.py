class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num < 4:
            return False
        if num % 2 != 0:
            return False
        while num >= 4:
            if num % 4 != 0:
                return False
            num = num // 4
        if num == 1:
            return True
        else:
            return False