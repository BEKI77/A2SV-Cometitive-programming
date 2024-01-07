class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans=0
        sum=0
        l,r=0,0
        while l<len(nums) and r<len(nums):
            if r-l==sum or sum+1==r-l:
                sum+=nums[r]
                r+=1
            else:
                sum-=nums[l]
                l+=1
            ans = max(ans,sum)
        
        if len(nums)==ans:
            return ans-1
        else:
            return ans