class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return nums
        move = False
        i = len(nums) - 1
        #index = i
        while i >= 0:
            if nums[i] != 0:
                move = True
            else:
                if move == True:
                    nums.pop(i)
                    nums.append(0)
            i = i - 1