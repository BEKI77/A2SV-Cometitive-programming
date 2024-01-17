class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        rSum,ans=0,0
        for i in range(len(nums)):
            rSum+=nums[i]
            ans+=mp[rSum-k]
            mp[rSum]+=1

        return ans