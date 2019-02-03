class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = []
        for a in A:
            B.append(a**2)
        B.sort()
        return B