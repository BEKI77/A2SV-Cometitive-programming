class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dist = len(set(nums))
        dic = defaultdict(int)
        l,r = 0,0
        ans = 0
        while l<n and r<n:
            dic[nums[r]]+=1
            while l<=r and len(dic)==dist:
                ans+= (n-r)
                dic[nums[l]]-=1
                if dic[nums[l]]==0:
                    del dic[nums[l]]
                l+=1
            r+=1
        return ans