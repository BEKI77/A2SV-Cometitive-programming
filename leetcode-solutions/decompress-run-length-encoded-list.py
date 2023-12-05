class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            if i*2+1 < len(nums):
                for j in range(nums[i*2]):
                    ans.append(nums[i*2+1])
        return ans