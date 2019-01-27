class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            if res < 2 or num != nums[res - 2]:
                nums[res] = num
                res += 1
        return res