class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[0] >= 0:  # all numbers in nums greater than or equal to zero
            return nums[-1] * nums[-2] * nums[-3]
        else:
            if nums[1] >= 0:  # only one number in nums is negative
                return nums[-1] * nums[-2] * nums[-3]
            else:  # there are at least two numbers in nums are negative
                if (nums[0] * nums[1] * nums[-1]) > (nums[-1] * nums[-2] * nums[-3]):
                    return nums[0] * nums[1] * nums[-1]
                else:
                    return nums[-1] * nums[-2] * nums[-3]
