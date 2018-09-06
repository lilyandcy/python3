class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k == 0 or k % len(nums) == 0:
            nums = nums
        else:
            rot = k % len(nums)
            for i in range(rot):
                nums.insert(0, nums[-1])
                nums.pop()