class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans= set()
        nums.sort()
        for i in range(len(nums)):
            l,r= i+1, len(nums)-1
            while l<r:
                sum = nums[i]+nums[l]+nums[r]
                if sum==0:
                    ans.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif sum>0:
                    r-=1
                else:
                    l+=1
        return list(ans)