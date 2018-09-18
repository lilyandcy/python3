class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        n = len(A[0])
        B = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            for j in range(n):
                B[j][i] = A[i][j]
        return B