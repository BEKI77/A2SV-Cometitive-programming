class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ph=0
        se=0
        while se<len(nums) and  ph<len(nums):
            if nums[se]==0:
                se+=1
            elif nums[ph]==0:
                nums[se],nums[ph] = nums[ph],nums[se]
                ph+=1
            else:
                se+=1
                ph+=1
                
        