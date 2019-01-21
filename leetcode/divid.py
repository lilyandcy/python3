class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend
        res = 0
        if abs(dividend) < abs(divisor):
            return 0
        if dividend < 0 and divisor < 0:
            ###
            dividend = abs(dividend)
            divisor = abs(divisor)
            while dividend - divisor >= 0:
                res += 1
                dividend -= divisor
            return res
        elif dividend > 0 and divisor > 0:
            ###
            while dividend - divisor >= 0:
                res += 1
                dividend -= divisor
            return res
        else:
            dividend = abs(dividend)
            divisor = abs(divisor)
            while dividend - divisor >= 0:
                res += 1
                dividend -= divisor
            return -res