class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        high = num // 2
        low = 1
        while high > low:
            if num == high ** 2:
                return True
            elif num < high ** 2:
                high = high // 2
            else:
                low = high
                high += 1
        return False