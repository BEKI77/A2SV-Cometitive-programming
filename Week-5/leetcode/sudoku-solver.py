class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        li = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=='.':
                    li.append([r,c])

        def isVal(row, col,chk):

            for i in range(len(board[row])):
                if chk== board[row][i]:
                    return False
            for i in range(len(board)):
                if chk== board[i][col]:
                    return False

        #here i hard coded the possible grid combinations that are valid for the given row and col
            table = {(0,0):[[0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]],
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
        
        def backtrack(i):
            if i==len(li):
                return True
             
            r,c = li[i][0], li[i][1]    
            for z in range(1,10):
                if isVal(r,c,str(z)):
                    board[r][c] = str(z)
                    if backtrack(i+1):
                        return True
                        
                    board[r][c]= "."
                   
        # print(li)
        backtrack(0)
      