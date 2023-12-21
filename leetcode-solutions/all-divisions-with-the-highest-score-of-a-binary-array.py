class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans=defaultdict(list)
        pSum=[0 for _ in range(n)]
        pSum[0]=nums[0]
        for i in range(1,n):
            pSum[i] = pSum[i-1] + nums[i]
    
        for i in range(n):
            if i==0:
                ans[pSum[n-1]].append(i)
            else:
                ans[abs(i-pSum[i-1]) + pSum[n-1]-pSum[i-1]].append(i)

        ans[n-pSum[n-1]].append(n)
        
        mx = max( i for i,val in ans.items())
        res=[]
        for i,val in ans.items():
            if i==mx:
                for j in val:
                    res.append(j)
        return res