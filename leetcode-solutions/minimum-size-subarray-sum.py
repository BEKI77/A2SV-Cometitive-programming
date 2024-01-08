class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        sum,ans=0,inf
        while l<len(nums) and r<len(nums):
            if sum+nums[r]<target:
                sum+=nums[r]
                r+=1
            else:
                ans=min(ans,r-l+1)
                sum-=nums[l]
                l+=1
        if ans==inf:
            return 0
        else:
            return ans