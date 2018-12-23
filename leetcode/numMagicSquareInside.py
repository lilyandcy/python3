class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid[0]) < 3 or len(grid) < 3:
            return 0
        res = 0
        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):
                magicGrid = [[grid[row+i][col+j] for j in range(3)] for i in range(3)]
                if self.isSquare(magicGrid):
                    res += 1
        return res

    def isSquare(self, grid):
        oneGrid = grid[0]
        oneGrid.extend(grid[1])
        oneGrid.extend(grid[2])
        if len(set(oneGrid)) != 9 or sum(oneGrid) != 45 or max(oneGrid) > 9 or min(oneGrid) < 1:
            return False
        else:
            line1 = grid[0][0] + grid[0][1] + grid[0][2]
            line2 = grid[1][0] + grid[1][1] + grid[1][2]
            line3 = grid[2][0] + grid[2][1] + grid[2][2]
            column1 = grid[0][0] + grid[1][0] + grid[2][0]
            column2 = grid[0][1] + grid[1][1] + grid[2][1]
            column3 = grid[0][2] + grid[1][2] + grid[2][2]
            cross1 = grid[0][0] + grid[1][1] + grid[2][2]
            cross2 = grid[0][2] + grid[1][1] + grid[2][0]
            if line1 == line2 == line3 == column1 == column2 == column3 == cross1 == cross2:
                return True
            else:
                return False
