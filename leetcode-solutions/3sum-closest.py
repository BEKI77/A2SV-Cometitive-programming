class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sum,prevDif = 0,inf
        nums.sort()
        for i in range(len(nums)):
            l,r = i+1,len(nums)-1
            while l<r:
                curSum = nums[i]+nums[l]+nums[r]
                diff = abs(target-curSum)
                if diff<prevDif:
                    sum=curSum
                    prevDif = diff
                if target>curSum:
                    l+=1
                else:
                    r-=1
        
        return sum