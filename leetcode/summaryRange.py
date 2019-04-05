class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if nums == []:
            return res
        start = nums[0]
        end = nums[-1]
        count = 1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                count += 1
            else:
                if count == 1:
                    blockStr = str(nums[i])
                    res.append(blockStr)
                else:
                    blockStr = str(nums[i-count+1]) + "->" + str(nums[i])
                    res.append(blockStr)
                    count = 1
        if count == 1:
            blockStr = str(nums[-1])
            res.append(blockStr)
        else:
            blockStr = str(nums[-1-count+1]) + "->" + str(nums[-1])
            res.append(blockStr)
        return res