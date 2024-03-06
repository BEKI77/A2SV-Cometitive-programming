class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isSafe(r,c, board,n):
            for i in range(c):
                if board[r][i]=='Q':
                    return False

            i, j = r, c
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            i, j = r, c
            while i<n and j>-1:
                if board[i][j]=='Q':
                    return False
                i+=1
                j-=1

            return True

        def backtrack(c,n):
            if c == n:
                temp = []
                for i in range(len(board)):
                    temp.append( "".join(board[i]))
                ans.append(temp)
                print(ans)
            for k in range(n):
                if isSafe(k,c,board,n):
                    board[k][c]='Q'
                    backtrack(c+1,n)
                    board[k][c]='.'

        ans = []
        board = [['.' for _ in range(n)]for _ in range(n)]
        backtrack(0,n)
        return ans