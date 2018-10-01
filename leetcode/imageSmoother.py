class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        rM = [[0 for i in range(len(M[0]))] for j in range(len(M))]
        print(rM)
        height = len(M)
        width = len(M[0])
        for i in range(height):
            for j in range(width):
                count = 1
                rM[i][j] = M[i][j]
                if i - 1 >= 0:
                    rM[i][j] += M[i - 1][j]
                    count += 1
                if j - 1 >= 0:
                    rM[i][j] += M[i][j - 1]
                    count += 1
                if i + 1 < height:
                    rM[i][j] += M[i + 1][j]
                    count += 1
                if j + 1 < width:
                    rM[i][j] += M[i][j + 1]
                    count += 1
                if i - 1 >= 0 and j + 1 < width:
                    rM[i][j] += M[i - 1][j + 1]
                    count += 1
                if i - 1 >= 0 and j - 1 >= 0:
                    rM[i][j] += M[i - 1][j - 1]
                    count += 1
                if i + 1 < height and j - 1 >= 0:
                    rM[i][j] += M[i + 1][j - 1]
                    count += 1
                if i + 1 < height and j + 1 < width:
                    rM[i][j] += M[i + 1][j + 1]
                    count += 1
                rM[i][j] = rM[i][j] // count
        return rM
