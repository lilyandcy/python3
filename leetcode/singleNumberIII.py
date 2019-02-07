class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        res = []
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                i += 2
            else:
                res.append(nums[i])
                count += 1
                if count == 2:
                    return res
                i += 1
        if i == len(nums) - 1:
            res.append(nums[-1])
            return res