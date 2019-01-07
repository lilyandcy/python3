class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        sumNums = sum(nums)
        lsum = 0
        for i in range(length):
            if lsum * 2 == sumNums - nums[i]:
                return i
            lsum += nums[i]
        return -1