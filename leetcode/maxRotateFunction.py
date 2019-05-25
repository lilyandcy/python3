class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        # F(k+1) - F(k) = sum(A) - n * A[-k-1]
        s = sum(A)
        n = len(A)
        f = sum(i*A[i] for i in range(n))
        ans = f
        for i in range(1, n):
            f = f + s - n * A[-i]
            ans = max(ans, f)
        return ans