class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        if A[0] == 0:
            return sum(A)
        if A[0] > 0 and K % 2 == 0:
            return sum(A)
        if A[0] > 0 and K % 2 != 0:
            return sum(A[1:]) - A[0]
        for i in range(len(A)):
            if A[i] < 0 and K > 0:
                A[i] = -A[i]
                K -= 1
        if K % 2 == 0:
            return sum(A)
        else:
            A.sort()
            return sum(A[1:]) - A[0]