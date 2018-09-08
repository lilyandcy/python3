class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        rnum = 0
        used = []
        for i in range(len(nums)-1):
            for num in nums[i+1:]:
                if abs(nums[i]-num) == k:
                    if [min(nums[i],num), max(nums[i],num)] not in used:
                        used.append([min(nums[i],num), max(nums[i],num)])
                        rnum = rnum + 1
        return rnum