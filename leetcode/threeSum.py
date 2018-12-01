class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    if s == 0:
                        res.append([nums[i], nums[l], nums[r]])
                        l = l + 1
                        r = r - 1
                        while l < r and nums[l] == nums[l-1]:
                            l = l + 1
                        while r > l and nums[r] == nums[r+1]:
                            r = r - 1
                    elif s > 0:
                        r = r - 1
                    else:
                        l = l + 1
        return res