class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans,sum = nums[0],0
        for i in range(len(nums)):
            sum += nums[i]
            if ans<sum: 
                ans = sum
            if sum<0:
                sum=0
        return ans