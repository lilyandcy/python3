class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        numsLen = len(nums)
        if numsLen == 0:
            return 0
        i = 1
        count = 1
        max_count = 1
        while i < numsLen:
            if nums[i] > nums[i-1]:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 1
            i += 1
        max_count = max(count, max_count)
        return max_count