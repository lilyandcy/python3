class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        res = 0
        RCol = None
        RRow = None
        for i in range(8):
            if "R" in board[i]:
                RRow = i
                break
        RCol = board[RRow].index("R")
        strRow = "".join(board[RRow])
        strRow = strRow.replace(".", "")
        if "Rp" in strRow:
            res += 1
        if "pR" in strRow:
            res += 1
        strCol = "".join(i[RCol] for i in board)
        strCol = strCol.replace(".","")
        if "Rp" in strCol:
            res += 1
        if "pR" in strCol:
            res += 1
        return res