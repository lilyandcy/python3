class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numsLen = len(nums)
        i = 0
        while i < numsLen:
            if nums[i] != i:
                temp = nums[nums[i]]
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                nums[nums[i]] = nums[i]
                nums[i] = temp
            else:
                i = i + 1