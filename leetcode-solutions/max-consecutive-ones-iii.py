class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans,no_zeros,l = 0,0,0
        for i in range(len(nums)):
            if nums[i]==0:
                no_zeros+=1
            while no_zeros>k:
                if nums[l]==0:
                    no_zeros-=1
                l+=1
            ans = max(ans, i-l+1)
            
        return ans