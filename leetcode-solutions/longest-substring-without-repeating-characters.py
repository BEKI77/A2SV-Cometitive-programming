class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chk =set()
        ans=0
        l,r=0,0
        while r<len(s):
            if s[r] not in chk:
                chk.add(s[r])
                r+=1
            else:
                chk.remove(s[l])
                l+=1
            ans = max(ans,r-l)
        return ans