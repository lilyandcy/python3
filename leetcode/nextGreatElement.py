class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if nums == []:
            return []
        maxNums = max(nums)
        res = []
        baseNums = nums + nums
        for i in range(len(nums)):
            if nums[i] == maxNums:
                res.append(-1)
            else:
                for j in range(i+1, len(baseNums)):
                    if baseNums[j] > nums[i]:
                        res.append(baseNums[j])
                        break
        return res