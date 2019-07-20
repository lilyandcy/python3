class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        temp = [[i for i in j] for j in board]
        h = len(board)
        w = len(board[0])
        for i in range(h):
           for j in range(w):
               status = temp[i][j]
               a = i-1 if i-1>=0 else 0
               b = j-1 if j-1>=0 else 0
               c = i+1 if i+1<=h-1 else h-1
               d = j+1 if j+1<=w-1 else w-1
               num = -status
               for m in range(a,c+1):
                   for n in range(b,d+1):
                       num += temp[m][n]
               if status==1 and num<2:
                   board[i][j]=0
               if status==1 and num>3:
                   board[i][j]=0
               if status==0 and num==3:
                   board[i][j]=1