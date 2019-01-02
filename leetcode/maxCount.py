class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        for tup in ops:
            if tup[0] < m:
                m = tup[0]
            if tup[1] < n:
                n = tup[1]
        return m * n