class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val not in nums:
            return len(nums)
        elementcount = nums.count(val)
        for i in range(elementcount):
            nums.remove(val)
        return len(nums)