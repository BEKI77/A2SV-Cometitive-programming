class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        hourglass = [[-1,-1],[-1,0],[-1,1],[0,0],[1,-1],[1,0],[1,1]]
        mx = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r>0 and c>0 and r<len(grid)-1 and c<len(grid[0])-1:
                    cur=0
                    for i in hourglass:
                        cur+=grid[r+i[0]][c+i[1]]
                    mx = max(mx,cur)
        return mx