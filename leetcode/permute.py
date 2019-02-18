class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length == 1 or length == 0:
            return [nums]
        res = []
        for i in range(length):
            list_one = self.permute(nums[0:i]+nums[i+1:])
            for j in list_one:
                res.append([nums[i]]+j)
        return res