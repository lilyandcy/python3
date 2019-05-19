class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp[i][j] represents the max line length of the square and the point is bottom right
        # dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        if not matrix:
            return 0
        dp = [[0]*(len(matrix[0])+1) for i in range(len(matrix)+1)]
        max_len = 0
        # 从(1,1)开始
        # |
        for i in range(1, len(dp)):
            # ->
            for j in range(1, len(dp[0])):
                # 注意是字符串类型的1，不是整形！！
                if matrix[i-1][j-1] == '1':
                    # 一个 1 出现，能成就的最长边是它 上 下 对角线 三个点的最小值 +1
                    # 如果三个老点至少一个为 0，这个 1 就不能构成边，但还是要+1给以后的点用
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    # 每次有 1 出现就要更新最长边，也就是最大面积
                    max_len = max(max_len, dp[i][j])
        # 正方形的面积是边的平方
        return max_len**2