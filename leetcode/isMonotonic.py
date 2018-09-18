class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        sortA = A.copy()
        sortA.sort()
        if sortA == A:
            return True
        else:
            sortA.sort(reverse=True)
            if sortA == A:
                return True
        return False