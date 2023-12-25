class Solution:
    def valid(self,board, row, col)->bool:
        chk = board[row][col]
        for i in range(len(board[row])):
            if chk== board[row][i] and i!=col:
                return False
        for i in range(len(board)):
            if chk== board[i][col] and i!=row:
                return False

        table = {  (0,0):[[0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]],
                    (0,1):[[0,-1], [0,1], [1,-1], [1,0], [1,1], [2,-1], [2,0], [2,1]],
                    (0,2):[[0,-1], [0,-2], [1,-2], [1,-1], [1,0], [2,-2], [2,-1], [2,0]],
                    (1,0):[[-1,0], [-1,1], [-1,2], [0,1], [0,2], [1,0], [1,1], [1,2]],
                    (1,1):[[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]],
                    (1,2):[[-1,-2], [-1,-1], [-1,0], [0,-2], [0,-1], [1,-2], [1,-1], [1,0]],
                    (2,0):[[-2,0], [-2,1], [-2,2], [-1,0], [-1,1], [-1,2], [0,1], [0,2]],
                    (2,1):[[-2,-1], [-2,0], [-2,1], [-1,-1], [-1,0], [-1,1], [0,-1], [0,1]],
                    (2,2):[[-2,-2],[-2,-1],[-2,0],[-1,-2],[-1,-1],[-1,0],[0,-2],[0,-1]]
        }
        for i in table[(row%3,col%3)]:
            if chk == board[row+i[0]][col+i[1]]:
                return False
        return True
     
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        fl = True
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]!='.':
                    fl = self.valid(board, row, col)
                    if not fl: return False
        return True
