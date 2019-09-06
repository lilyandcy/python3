class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        res = 0
        if len(calories) < k:
            return res
        s = sum(calories[0:k])
        if s < lower:
            res -= 1
        elif s > upper:
            res += 1
        for i in range(1, len(calories)-k+1):
            s = s - calories[i-1] + calories[i-1+k]
            if s < lower:
                res -= 1
            elif s > upper:
                res += 1
        return res