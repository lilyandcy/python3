class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 2:
            i = n % 2
            j = (n // 2) % 2
            if i == j:
                return False
            n = n // 2
        return True