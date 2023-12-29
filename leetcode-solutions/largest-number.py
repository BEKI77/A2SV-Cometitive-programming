class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if str(nums[j])+str(nums[j+1])<str(nums[j+1])+str(nums[j]):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        if nums[0]==0: return "0"
        else: return ''.join([str(i) for i in nums])

        