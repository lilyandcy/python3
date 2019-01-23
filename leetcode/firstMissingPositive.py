class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 1
        maxNum = max(nums)
        if maxNum < 1:
            return 1
        for i in range(1,maxNum):
            if i not in nums:
                return i
        return maxNum + 1