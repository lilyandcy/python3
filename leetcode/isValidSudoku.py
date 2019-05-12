class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # Validate Row
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i].count(board[i][j]) > 1:
                        return False
        # Validate Column
        tempCol = []
        for j in range(9):
            for i in range(9):
                if board[i][j] != '.':
                    tempCol.append(board[i][j])
            for k in range(len(tempCol)):
                if tempCol.count(tempCol[k]) > 1:
                    return False
            tempCol = []

        # Validate Block
        tempBlk = []
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] != '.':
                    tempBlk.append(board[i][j])
        for k in range(len(tempBlk)):
            if tempBlk.count(tempBlk[k]) > 1:
                return False
        tempBlk = []

        for i in range(0,3):
            for j in range(3,6):
                if board[i][j] != '.':
                    tempBlk.append(board[i][j])
        for k in range(len(tempBlk)):
            if tempBlk.count(tempBlk[k]) > 1:
                return False
        tempBlk = []

        for i in range(0,3):
            for j in range(6,9):
                if board[i][j] != '.':
                    tempBlk.append(board[i][j])
        for k in range(len(tempBlk)):
            if tempBlk.count(tempBlk[k]) > 1:
                return False
        tempBlk = []

        for i in range(3,6):
            for j in range(0,3):
                if board[i][j] != '.':
                    tempBlk.append(board[i][j])
        for k in range(len(tempBlk)):
            if tempBlk.count(tempBlk[k]) > 1:
                return False
        tempBlk = []

        for i in range(3,6):
            for j in range(3,6):
                if board[i][j] != '.':
                    tempBlk.append(board[i][j])
        for k in range(len(tempBlk)):
            if tempBlk.count(tempBlk[k]) > 1:
                return False
        tempBlk = []

        for i in range(3,6):
            for j in range(6,9):
                if board[i][j] != '.':
                    tempBlk.append(board[i][j])
        for k in range(len(tempBlk)):
            if tempBlk.count(tempBlk[k]) > 1:
                return False
        tempBlk = []

        for i in range(6,9):
            for j in range(0,3):
                if board[i][j] != '.':
                    tempBlk.append(board[i][j])
        for k in range(len(tempBlk)):
            if tempBlk.count(tempBlk[k]) > 1:
                return False
        tempBlk = []

        for i in range(6,9):
            for j in range(3,6):
                if board[i][j] != '.':
                    tempBlk.append(board[i][j])
        for k in range(len(tempBlk)):
            if tempBlk.count(tempBlk[k]) > 1:
                return False
        tempBlk = []

        for i in range(6,9):
            for j in range(6,9):
                if board[i][j] != '.':
                    tempBlk.append(board[i][j])
        for k in range(len(tempBlk)):
            if tempBlk.count(tempBlk[k]) > 1:
                return False
        tempBlk = []

        return True