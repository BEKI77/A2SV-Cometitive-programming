class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        li1 = []
        li2 = []
        nextMin = [-1]*(n)
        for i in range(n):
            next_val = heights[i]
            while li1 and heights[li1[-1]] >= next_val:
                nextMin[li1.pop()] = i
 
            li1.append(i)

        prvMin = [-1]*(n)

        for i in range(n):
            next_val = heights[i]
            while li2 and heights[li2[-1]] >= next_val:
                li2.pop()
        
            prvMin[i] = li2[-1] if li2 else -1
            li2.append(i)

        ans = 0

        for i in range(n):
            # print(prvMin[i], heights[i], nextMin[i])
            if prvMin[i]==-1 and nextMin[i]==-1:
                ans = max(ans, heights[i]*n )
            elif nextMin[i]==-1:
                ans = max(ans,heights[i]*(n-prvMin[i]-1))
            elif prvMin[i]==-1:
                ans = max(ans, heights[i]*(nextMin[i]) )
            else:
                ans = max(ans, heights[i]*(nextMin[i]-prvMin[i]-1))

    
        return ans