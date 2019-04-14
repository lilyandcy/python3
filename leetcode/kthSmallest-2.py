class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        listM = matrix[0]
        i = 1
        while i < len(matrix):
            listM.extend(matrix[i])
            i += 1
        listM.sort()
        return listM[k-1]