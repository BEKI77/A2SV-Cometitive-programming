class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sum,ans,l = 0,0,0
        table = set()
        for i in range(len(nums)):
            if nums[i] not in table:
                sum+=nums[i]
                table.add(nums[i])
            else:
                while l<len(nums) and nums[l] != nums[i]:
                    table.remove(nums[l])
                    sum-=nums[l]
                    l+=1
                l+=1            
            ans = max(ans,sum)
        return ans
        

