class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        mLocation = []
        nLocation = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i not in mLocation:
                        mLocation.append(i)
                    if j not in nLocation:
                        nLocation.append(j)
        for row in mLocation:
            matrix[row] = [0] * n
        for col in nLocation:
            for i in range(m):
                matrix[i][col] = 0