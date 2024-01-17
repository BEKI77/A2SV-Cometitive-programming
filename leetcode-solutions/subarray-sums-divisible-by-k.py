class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rSum,ans=0,0
        mp = defaultdict(int)
        mp[0]=1
        for i in range(len(nums)):
            rSum+=(nums[i]%k+k)%k
            ans+=mp[rSum%k]
            mp[rSum%k]+=1
        return ans