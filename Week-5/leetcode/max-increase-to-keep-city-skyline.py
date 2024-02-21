class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        mxC = [0]*(n)
        mxR = [0]*(n)
        for r in range(n):
            for c in range(n):
                mxC[c] = max(mxC[c], grid[r][c])
                mxR[r] = max(mxR[r], grid[r][c])

        for r in range(n):
            for c in range(n):
                temp = min(mxR[r], mxC[c])
                if grid[r][c]!= temp:
                    val = temp - grid[r][c]
                    ans+=val     
        return ans