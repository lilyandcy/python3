class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        row_max = []
        col_max = []
        length = len(grid)
        for i in range(length):
            row_max.append(max(grid[i]))
            temp = 0
            for j in range(length):
                temp = max(temp, grid[j][i])
            col_max.append(temp)
        for k in range(length):
            for j in range(length):
                res += min(row_max[k], col_max[j]) - grid[k][j]
        return res