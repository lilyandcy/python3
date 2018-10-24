class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0;
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            lst = [];
            lst.append(nums[0])
            lst.append(max(nums[0], nums[1]))
            i = 2
            while i < len(nums):
                lst.append(max(nums[i] + lst[i - 2], lst[i - 1]))
                i += 1
            return lst[len(nums) - 1]