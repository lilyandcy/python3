class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        if num == 0:
            return "0"
        if num < 0:
            num = abs(num)
            while num != 0:
                mod7 = num % 7
                res = str(mod7) + res
                num //= 7
            res = "-" + res
        else:
            while num != 0:
                mod7 = num % 7
                res = str(mod7) + res
                num //= 7
        return res