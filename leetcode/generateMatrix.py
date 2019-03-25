class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        u = 0
        d = n-1
        l = 0
        r = n-1
        matrix =[[0]*n for i in range(n)]
        index = 0
        while index < n*n:
            for i in range(l, r+1):
                index += 1
                matrix[u][i] = index
            u += 1

            for i in range(u, d+1):
                index += 1
                matrix[i][r] = index
            r -= 1

            for i in range(r, l-1, -1):
                index += 1
                matrix[d][i] = index
            d -= 1

            for i in range(d, u-1, -1):
                index += 1
                matrix[i][l] = index
            l += 1
        return matrix