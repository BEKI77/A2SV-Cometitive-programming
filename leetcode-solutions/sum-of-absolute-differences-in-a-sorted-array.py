class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pSum = [0]*(n+1)
        for i in range(n):
            pSum[i+1]=pSum[i]+nums[i]
        ans =[0]*n
        for i in range(n):
            ans[i]= (nums[i]*i)-pSum[i] + (pSum[-1] - pSum[i]) - (nums[i]*(n-i))
        return ans
        