class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranks = nums.copy()
        ranks.sort(reverse = True)
        ranksDict = {}
        for i in range(len(ranks)):
            if i == 0:
                ranksDict[ranks[i]] = "Gold Medal"
            else:
                if i == 1:
                    ranksDict[ranks[i]] = "Silver Medal"
                elif i == 2:
                    ranksDict[ranks[i]] = "Bronze Medal"
                else:
                    ranksDict[ranks[i]] = str(i+1)
        for i in range(len(nums)):
            nums[i] = ranksDict[nums[i]]
        return nums
