class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans,pSum=0,0
        for i in range(len(nums)):
            pSum+=nums[i]
            ans = max(ans,(pSum+i)//(i+1))
            
        return ans