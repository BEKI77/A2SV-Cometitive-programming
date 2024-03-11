class Solution:
    def trap(self, height: List[int]) -> int:
        li = []
        n = len(height)
        mxl,mxr = -inf,-inf
        li1 = [-1]*(n)
        li2 = [-1]*(n)
        res = 0
        for i in range(n):
            mxl = max(mxl,height[i])
            mxr = max(mxr, height[n-i-1])
            li1[i]=mxl
            li2[n-i-1]=mxr
        for i in range(n):
            res+=min(li1[i],li2[i])-height[i]
        return res