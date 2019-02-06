class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maxSum = sum(nums[0:k])
        maxAvg = maxSum / k
        for i in range(k, len(nums)):
            maxSum -= nums[i-k]
            maxSum += nums[i]
            avg = maxSum / k
            if avg > maxAvg:
                maxAvg = avg
        return maxAvg