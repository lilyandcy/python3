class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        l = [a, b, c]
        l.sort()
        if l[1] == l[0] + 1 and l[1] == l[2] - 1:
            return [0,0]
        if l[1] == l[0] + 1 or l[1] == l[2] - 1 or l[1] == l[0] + 2 or l[1] == l[2] - 2:
            return [1, l[2] - l[0] - 2]
        return [2, l[2] - l[0] - 2]