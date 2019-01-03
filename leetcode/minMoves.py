class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minValue = min(nums)
        occurrence = 0
        for i in range(len(nums)):
            temp = nums[i] - minValue
            occurrence += temp
        return occurrence