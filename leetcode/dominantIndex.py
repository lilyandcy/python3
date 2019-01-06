class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        maxn = max(nums)
        tempnums = nums.copy()
        tempnums.remove(maxn)
        maxtemp = max(tempnums) * 2
        if maxn >= maxtemp:
            return nums.index(maxn)
        else:
            return -1