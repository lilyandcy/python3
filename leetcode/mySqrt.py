class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        l = 1
        r = x
        while l <= x:
            num = (l + r) // 2
            s = num **2
            if s <= x < (num+1) **2:
                return num
            if s < x:
                l = num
            if s > x:
                r = num