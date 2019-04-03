class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == [[]]:
            return False
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                left = 0
                right = len(matrix[0]) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if target < matrix[i][mid]:
                        right = mid - 1
                    elif target > matrix[i][mid]:
                        left = mid + 1
                    else:
                        return True
        return False