class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        chk=set()
        ans=0
        for i in nums:
            chk.add(i)

        for i in nums:
            if i-1 not in chk:
                cur=0
                while i in chk:
                    cur+=1
                    i+=1
                ans = max(ans,cur)
        return ans