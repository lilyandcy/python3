class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        m = l // 2
        beforeM = sum(nums[:m])
        afterM = sum(nums[m+1:])
        if l % 2 != 0:
            return afterM - beforeM
        else:
            return afterM - beforeM + nums[m]