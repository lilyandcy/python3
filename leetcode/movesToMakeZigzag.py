class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n1 = 0
        n2 = 0
        nums1 = nums.copy()
        for i in range(1, len(nums1), 2):
            if nums1[i-1] >= nums1[i]:
                n1 += nums1[i-1] - nums1[i] + 1
                nums1[i-1] -= nums1[i-1] - nums1[i] + 1
            if i + 1 < len(nums1) and nums1[i+1] >= nums1[i]:
                n1 += nums1[i+1] - nums1[i] + 1
                nums1[i+1] -= nums1[i+1] - nums1[i] + 1
        for j in range(0, len(nums), 2):
            if j > 0 and nums[j-1] >= nums[j]:
                n2 += nums[j-1] - nums[j] + 1
                nums[j-1] -= nums[j-1] - nums[j] + 1
            if j + 1 < len(nums) and nums[j+1] >= nums[j]:
                n2 += nums[j+1] - nums[j] + 1
                nums[j+1] -= nums[j+1] - nums[j] + 1
        return min(n1, n2)