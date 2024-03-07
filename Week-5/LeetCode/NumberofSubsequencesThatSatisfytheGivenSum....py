class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        MOD = pow(10,9) + 7
        ans = 0
        for i in range(n):
            val = bisect_right(nums, target-nums[i])-1
            size = val-i +1
            ans += pow(2,size-1,MOD) if size>0 else 0

        return ans%MOD