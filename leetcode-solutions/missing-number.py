class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = len(nums)
        act=0
        for i in range(len(nums)):
            sum+=i
            act+=nums[i]
        return sum-act
