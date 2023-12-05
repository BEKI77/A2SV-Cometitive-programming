class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        chk = True
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if not chk:
                    return False
                if i==0 or nums[i+1] >= nums[i-1]:
                    nums[i]=nums[i+1]
                else:
                    nums[i+1]=nums[i]
                chk = False
           # else: continue
       
        return True
        
        