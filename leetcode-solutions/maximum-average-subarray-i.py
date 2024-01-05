class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win = sum(nums[:k])
        ans = win/k
        for i in range(k,len(nums)):
           win+=nums[i]
           win-=nums[i-k]
           ans = max(ans,win/k)
        return ans

