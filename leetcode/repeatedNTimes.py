class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A) // 2
        for e in A:
            if A.count(e) == N:
                return e