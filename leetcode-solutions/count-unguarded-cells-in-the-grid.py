class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        for i in walls:
            grid[i[0]][i[1]]=2
        for i in guards:
             grid[i[0]][i[1]]=2
        cnt=0
        for i in guards:
            j = i[0]-1
            while j>=0 and grid[j][i[1]]!=2:
                if grid[j][i[1]]==0:
                    grid[j][i[1]]=1
                    cnt+=1
                j-=1

            j = i[0]+1 
            while j<m and grid[j][i[1]]!=2:
                if grid[j][i[1]]==0:
                    grid[j][i[1]]=1
                    cnt+=1
                j+=1

            j = i[1]-1
            while j>=0 and grid[i[0]][j]!=2:
                if grid[i[0]][j]==0:
                    grid[i[0]][j]=1
                    cnt+=1
                j-=1

            j = i[1]+1
            while j<n and grid[i[0]][j]!=2: 
                if grid[i[0]][j]==0:
                    grid[i[0]][j]=1
                    cnt+=1
                j+=1

        return (m*n) -(cnt+len(walls)+len(guards))