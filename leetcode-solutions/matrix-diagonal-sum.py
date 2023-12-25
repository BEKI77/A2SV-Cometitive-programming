class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0 
        n = len(mat)
        for r in range(n):
            for c in range(n):
                if r==c:
                    res+=mat[r][c]
                if n-1-r==c:
                    res+=mat[r][c]
                if n-1-r == c and r==c:
                    res-=mat[r][c]
        return res