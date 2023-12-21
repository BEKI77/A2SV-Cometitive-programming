class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = inf
        min2 = inf
        for i in range(len(nums)):
            if min2<nums[i]:
                return True
            if nums[i]<=min1:
                 min1=nums[i]
            else:
                min2=nums[i]
            
        return False