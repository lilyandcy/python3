class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        length = len(A)
        if length < 3:
            return 0
        dp = [0] * length
        count = 0
        for i in range(2, length):
            if A[i] + A[i-2] == 2 * A[i-1]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 0
            count += dp[i]
        return count