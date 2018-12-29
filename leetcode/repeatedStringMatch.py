class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        res = 1
        if B in A:
            return res
        lenA = len(A)
        lenB = len(B)
        tempA = A
        while len(tempA) <= 2 * lenA + lenB + 1:
            tempA += A
            res += 1
            if B in tempA:
                return res
        return -1