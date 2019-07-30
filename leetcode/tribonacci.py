class Solution:
    def tribonacci(self, n: int) -> int:
        res = [0, 1, 1]
        if n < 3:
            return res[n]
        for i in range(3, n+1):
            val = res[-1] + res[-2] + res[-3]
            res.append(val)
        return res[-1]