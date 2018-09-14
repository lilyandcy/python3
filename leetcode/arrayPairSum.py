class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        i = 0
        while i <= len(nums) - 2:
            res = res + min(nums[i], nums[i+1])
            i = i + 2
        return res