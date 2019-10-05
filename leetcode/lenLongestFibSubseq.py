class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        res = 0
        a = [[0] * n for i in range(n)]
        for i in range(n):
            lo = 0
            hi = i - 1
            v = A[i]
            while lo < hi:
                if A[lo] + A[hi] < v:
                    lo += 1
                elif A[lo] + A[hi] > v:
                    hi -= 1
                else:
                    if a[lo][hi]:
                        a[hi][i] = a[lo][hi] + 1
                    else:
                        a[hi][i] = 3
                    res = max(a[hi][i], res)
                    lo += 1
                    hi -= 1
        return res