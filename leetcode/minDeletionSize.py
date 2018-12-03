class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if len(A) < 1:
            return 0
        if len(A[0]) < 1:
            return 0
        res = 0
        for j in range(len(A[0])):
            for i in range(len(A)-1):
                if A[i][j] > A[i+1][j]:
                    res += 1
                    break
        return res