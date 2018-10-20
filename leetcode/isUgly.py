class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num > 1:
            if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
                return False
            else:
                if num % 2 == 0:
                    num //= 2
                if num % 3 == 0:
                    num //= 3
                if num % 5 == 0:
                    num //= 5
        if num == 1:
            return True