class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * N
        G = [[] for _ in range(N)]
        for x, y in paths:
            G[x-1].append(y-1)
            G[y-1].append(x-1)
        for i in range(N):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in G[i]}).pop()
        return res