class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        srange = max(A) - min(A) - 2 * K
        if srange < 0:
            return 0
        else:
            return srange