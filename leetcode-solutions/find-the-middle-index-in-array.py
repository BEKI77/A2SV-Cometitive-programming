class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        psum=[0]*(len(nums)+1)
        for i in range(len(nums)):
            psum[i+1] = psum[i]+nums[i]
        
        for i in range(1,len(psum)):
            if psum[i-1]==(psum[-1]-psum[i]):
                return i-1
        return -1