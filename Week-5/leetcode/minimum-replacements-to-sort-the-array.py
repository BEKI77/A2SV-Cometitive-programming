class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans,curMax = 0, nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>curMax:
                temp = math.ceil(nums[i]/curMax)
                ans+= temp-1
                curMax = nums[i]//temp
            else:
                curMax = nums[i]
        return ans