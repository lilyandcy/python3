class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        lenA = len(A)
        lenB = len(B)
        if lenA != lenB:
            return False
        if A == B and len(list(set(A))) < lenA:
            return True

        a = []
        b = []
        for i in range(lenA):
            if A[i] != B[i]:
                a.append(A[i])
                b.append(B[i])
        if len(a) == len(b) == 2 and a == b[::-1]:
            return True
        else:
            return False