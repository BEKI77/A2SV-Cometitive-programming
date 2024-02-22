class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        li = []
        curMin = nums[0]
        for i in range(1,len(nums)):
            while li and nums[i]>=li[-1][0]:
                li.pop()
            if li and nums[i]<li[-1][0] and nums[i]>li[-1][1]:
                return True
            li.append([nums[i],curMin])
            curMin = min(curMin,nums[i])
        return False
