class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length == 1 or length == 0:
            return [nums]
        res = []
        for i in range(length):
            list_one = self.permuteUnique(nums[0:i]+nums[i+1:])
            for j in list_one:
                if [nums[i]] + j not in res:
                    res.append([nums[i]]+j)
        return res