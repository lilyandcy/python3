class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        res = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i] + duration - 1 < timeSeries[i+1]:
                res += duration
            else:
                res += timeSeries[i+1] - timeSeries[i]
        res += duration
        return res
