class Solution:
    def totalNQueens(self, n: int) -> int:
        def isSafe(r,c):
            nonlocal n
            for i in range(c):
                if board[r][i]=='Q':
                    return False

            i, j = r, c
            while i > -1 and j > -1:
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

        def backtrack(c):
            nonlocal n,ans
            if c == n:
                ans+=1
               
            for k in range(n):
                if isSafe(k,c):
                    board[k][c]='Q'
                    backtrack(c+1)
                    board[k][c]='.'

        ans = 0
        board = [['.' for _ in range(n)]for _ in range(n)]
        backtrack(0)
        return ans