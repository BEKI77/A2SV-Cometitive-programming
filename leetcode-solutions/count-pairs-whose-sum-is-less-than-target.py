class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        l,r=0,1
        ans=0
        while l<len(nums):
            if r<len(nums) and nums[l]+nums[r]<target:
                ans+=1
                r+=1
            elif r==len(nums):
                l+=1
                r=l+1
            else:
                r+=1

        return ans
        