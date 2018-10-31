class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 2 == 0 or n < 1:
            return False
        while n >= 3:
            if n % 3 != 0:
                return False
            else:
                n = n // 3
        return True