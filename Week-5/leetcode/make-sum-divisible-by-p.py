class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        cum = sum(nums)%p
        if cum==0: return 0
        s,ans = 0,len(nums)
        mp = defaultdict(int)
        mp[0] = -1
        for i in range(len(nums)):
            s+=nums[i]
            key = (s%p)-cum
            if key < 0:
                key+=p 
            if key in mp:
                ans = min(ans, i - mp[key])
            mp[s%p]=i

        return ans if ans<len(nums) else -1
        