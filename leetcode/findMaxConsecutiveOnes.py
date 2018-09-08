class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen = 0
        currentlen = 0
        for i in range(len(nums)):
                if nums[i] == 1:
                    currentlen = currentlen + 1
                else:
                    if maxlen < currentlen:
                        maxlen = currentlen
                        currentlen = 0
                    else:
                        currentlen = 0
        if maxlen < currentlen:
            maxlen = currentlen
        return maxlen