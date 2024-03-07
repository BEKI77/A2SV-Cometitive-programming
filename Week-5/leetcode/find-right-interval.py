class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        start = sorted((intervals[i][0],i) for i in range(n))
        end = [intervals[i][1] for i in range(n)]
        ans = []
        for i in range(n):
            val= bisect_left(start, (end[i],0))
            tmp,ind = start[val] if val<len(start) else (-1,-1)
            ans.append(ind)
        
        return ans
