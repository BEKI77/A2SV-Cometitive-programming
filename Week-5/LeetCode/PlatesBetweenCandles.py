class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        ans = []
        li=[0]*n
        rSum = 0
        wall = []
        for i in range(n):
            if s[i]=='*':
                rSum+=1
                li[i]=rSum
            else:
                wall.append(i)
                li[i]=rSum

        for i in range(len(queries)):
            l,r = queries[i][0], queries[i][1]
            left = bisect_left(wall, l)
            right = bisect_right(wall, r)-1
            
            if left<=right<len(wall) and wall[left]>=l and wall[right]<=r:
                ans.append(li[wall[right]]-li[wall[left]])
            else:
                ans.append(0)
            
            

        return ans