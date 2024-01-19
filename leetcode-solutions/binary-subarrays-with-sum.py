class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans,rSum = 0,goal
        l,r = 0,0
        for r in range(len(nums)):
            rSum-=nums[r]
            while rSum<0:
                rSum+=nums[l]
                l+=1
            ans += (r-l+1)
        l,r = 0,0
        lSum , res = goal-1,0
        if lSum<0:
            res=0
        else:
            for r in range(len(nums)):
                lSum-=nums[r]
                while lSum<0:
                    lSum+=nums[l]
                    l+=1
                res +=(r-l+1)
        return ans-res


# def atMost(S):
#             if S < 0: return 0
#             res = i = 0
#             for j in xrange(len(A)):
#                 S -= A[j]
#                 while S < 0:
#                     S += A[i]
#                     i += 1
#                 res += j - i + 1
#             return res
#         return atMost(S) - atMost(S - 1)