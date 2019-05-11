class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if matrix == []:
            return res
        res.extend(matrix[0])
        new = [reversed(i) for i in matrix[1:]]
        if new == []:
            return res
        r = self.spiralOrder([i for i in zip(*new)])
        res.extend(r)
        return res