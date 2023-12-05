class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        for i in range(len(nums)-1):
            temp = nums[i]+nums[i+1]
            if  i+2 < len(nums) and temp > nums[i+2]:
                ans = max(ans, temp+nums[i+2])
        return ans