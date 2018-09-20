class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        elen = len(A)
        for i in range(elen):
            A[i].reverse()
            for j in range(elen):
                A[i][j] = 1 - A[i][j]
        return A