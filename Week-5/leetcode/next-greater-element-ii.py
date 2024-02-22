class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)    
        ans = [-1]*n
        li = []
        for i in range(2*n):
            while li and nums[li[-1]]<nums[i%n]:
                ans[li.pop()] = nums[i%n]

            li.append(i%n)
        
        return ans