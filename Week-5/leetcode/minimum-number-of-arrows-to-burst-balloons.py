class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        ans,end = 1, points[0][1]
        for i in range(1,len(points)):
            if end < points[i][0]:
                ans+=1
                end = max(end,points[i][1])
     
        print(points)
        return ans