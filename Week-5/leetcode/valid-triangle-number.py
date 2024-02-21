class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        nums.sort()
        for i in range(n-1, 0,-1):
            left = 0
            right = i-1
            while left <right:
                if nums[left] + nums[right] > nums[i]:
                    ans+= right - left
                    right-=1
                else:
                    left+=1
        return ans