class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #handle some corner case first
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
            else:
                i = i + 1
        return len(nums)