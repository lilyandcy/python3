class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        nums = sorted(costs, key = lambda x:x[0]-x[1])
        l = len(nums)
        for i in range(l):
            res += nums[i][i//(l//2)]
        return res