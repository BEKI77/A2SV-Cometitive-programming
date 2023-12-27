class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = [i[0] for i in points]
        x.sort()
        ans=0
        for i in range(len(x)-1):
            ans=max(ans,x[i+1]- x[i])
        return ans
