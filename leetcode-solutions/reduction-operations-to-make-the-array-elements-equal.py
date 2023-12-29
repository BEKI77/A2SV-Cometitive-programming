class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0]==nums[-1]: return 0
        else: 
            ans,cnt=0,0
            for i in range(len(nums)-1):
                if nums[i]!=nums[i+1]:
                    cnt+=1
                ans+=cnt
            return ans