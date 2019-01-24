class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1, -1]
        if nums.count(target) == 1:
            return [nums.index(target), nums.index(target)]
        return [nums.index(target), nums.index(target) + nums.count(target)-1]