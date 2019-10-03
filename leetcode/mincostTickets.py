class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        res = [0] * (days[-1] + 31)
        dayset = set(days)

        for i in range(1, len(res)):
            if i not in dayset:
                res[i] += res[i-1]
            else:
                res[i] = min(res[i-1]+costs[0], res[i-7]+costs[1], res[i-30]+costs[2])
        return res[-1]