import bisect
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            temp1 = nums[i]
            for j in range(i+1,len(nums)):
                temp2 = nums[j]
                k = bisect.bisect_left(nums[j+1:], temp2+temp1)
                ans+=(k)
        return ans