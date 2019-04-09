class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        maxA = max(A)
        if A[0] == maxA or A[-1] == maxA:
            return False
        idxMax = A.index(maxA)
        bA = sorted(A[:idxMax])
        aA = sorted(A[idxMax+1:], reverse = True)
        if A[:idxMax] != bA or A[idxMax+1:] != aA:
            return False
        elif len(A[:idxMax]) != len(set(bA)) or len(A[idxMax+1:]) != len(set(aA)):
            return False
        return True