class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for i in range(len(nums)-1):
            if mx == 0 and nums[i]==0:
                return False
            else:
                mx = max(mx,nums[i])
                mx-=1
              

        return True