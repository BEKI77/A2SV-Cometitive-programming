class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mp = Counter(nums)
        for i in range(len(nums)):
            if mp[0]>0:
                nums[i]=0
                mp[0]-=1
            elif mp[1]>0:
                nums[i]=1
                mp[1]-=1
            elif mp[2]>0:
                nums[i]=2
                mp[2]-=1
        