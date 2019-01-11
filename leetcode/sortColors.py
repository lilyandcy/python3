class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        countZero = nums.count(0)
        countOne = nums.count(1)
        countTwo = len(nums) - countZero - countOne
        for i in range(len(nums)):
            if countZero > 0:
                nums[i] = 0
                countZero -= 1
            else:
                if countOne > 0:
                    nums[i] = 1
                    countOne -= 1
                else:
                    nums[i] = 2