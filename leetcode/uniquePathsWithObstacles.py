class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # DP, go through first line -> go through first column
        # any other point = upper point + left point if point is not obstacle
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        obstacleGrid[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[0][i] == 1:
                obstacleGrid[0][i] = 0
            else:
                obstacleGrid[0][i] = obstacleGrid[0][i-1]
        for j in range(1, n):
            if obstacleGrid[j][0] == 1:
                obstacleGrid[j][0] = 0
            else:
                obstacleGrid[j][0] = obstacleGrid[j-1][0]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[j][i] == 1:
                    obstacleGrid[j][i] = 0
                else:
                    obstacleGrid[j][i] = obstacleGrid[j-1][i] + obstacleGrid[j][i-1]
        return obstacleGrid[-1][-1]
