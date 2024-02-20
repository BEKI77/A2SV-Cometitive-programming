class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        cnt ,rem= 0,0
        while target>1 and maxDoubles>=1:
            temp = target%2
            target-=(target)//2
            target -= temp
            cnt+=1+temp
            maxDoubles-=1
    
        return cnt+target-1
        