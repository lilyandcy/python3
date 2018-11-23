class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        Sxy, Sxz, Syz = 0, 0, 0
        columnMax = 0
        N = len(grid)
        for i in range(N):
            rowMax = 0
            for j in range(N):
                if grid[i][j] != 0:
                    Sxy += 1
                if grid[i][j] > rowMax:
                    rowMax = grid[i][j]
            Sxz += rowMax
        for j in range(N):
            columnMax = 0
            for i in range(N):
                if grid[i][j] > columnMax:
                    columnMax = grid[i][j]
            Syz += columnMax
        return Sxy+Sxz+Syz