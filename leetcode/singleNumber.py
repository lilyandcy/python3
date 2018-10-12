class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 0^t = t, t ^ t = 0, as only y exists once, other x exists twice
        # the formular can be taken as 0^(x1^x1)^...^(xn^xn)^y = y
        res = 0
        for num in nums:
            res ^= num
        return res