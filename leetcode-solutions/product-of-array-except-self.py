class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        rprod = 1
        fl1 = False
        fl2 = False
        for i in range(len(nums)):
            if nums[i]!=0:
                rprod*=nums[i]
            elif fl1 and nums[i]==0:
                fl2 = True
                break
            elif nums[i]==0:
                fl1=True
        print(rprod)
        ans = [0]*len(nums)
        if fl2:
            return ans
        for i in range(len(nums)):
            if nums[i]!=0 and fl1:
                ans[i]=0
            elif nums[i]!=0:
                ans[i] =rprod//nums[i]
            elif nums[i]==0 and fl1:
                ans[i]=rprod
        return ans