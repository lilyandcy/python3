class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        origin = length * (length + 1) // 2
        errorSum = sum(nums)
        nodup = sum(set(nums))
        missing = origin - nodup
        error = errorSum - nodup
        return [error, missing]