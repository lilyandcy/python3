class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        if len(nums) == 1:
            return nums
        l = len(nums)
        nums.sort()

        dp = [[i] for i in nums]
        for i in range(1, l):
            for j in range(i - 1, -1, -1):
                if not nums[i] % nums[j]:
                    dp[i] = max(dp[j] + [nums[i]], dp[i], key=len)
        return max(dp, key=len)