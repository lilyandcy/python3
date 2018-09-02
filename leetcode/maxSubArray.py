class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return nums[0]
        sumn = 0
        maxn = nums[0]
        for i in range(len(nums)):
            if sumn < 0:
                sumn = 0
            sumn = sumn + nums[i]
            maxn = max(maxn, sumn)

        return maxn