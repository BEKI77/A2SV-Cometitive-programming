class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        fSum = [0]*(len(nums)+1)
        for i in range(len(requests)):
            fSum[requests[i][0]]+=1
            fSum[requests[i][1]+1]-=1
        for i in range(1,len(fSum)):
            fSum[i]+=fSum[i-1]
        ans = 0
        fSum.sort(reverse = True)
        nums.sort(reverse = True)
        for i in range(len(nums)):
            if fSum[i]==0:
                break
            ans+=(nums[i]*fSum[i])
            
        return ans%((10**9)+7)