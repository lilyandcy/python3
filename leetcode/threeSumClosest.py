class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        import math
        res = sum(nums[:2]) + nums[-1] - target
        n = len(nums)
        i = 0
        while i <= n - 3:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            if nums[i] + nums[i+1] + nums[i+2] - target >= abs(res):
                break
            j = i + 1
            k = n - 1
            while j < k:
                t = nums[i] + nums[j] + nums[k]
                if t - target == 0:
                    return target
                elif abs(t-target) < abs(res):
                    res = t - target
                if t - target > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
        return res + target