class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        res = []
        start = 0
        n = len(S)
        for i in range(1, n):
            if S[i] != S[i-1]:
                if i - start >= 3:
                    res.append([start, i-1])
                start = i
        if n - start >=3:
            res.append([start, n-1])
        return res