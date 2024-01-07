class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        chk = set(["a","e","i","o","u"])
        cur,ans=0,0
        l,r=0,0
        while r<len(s):
            if r-l<k:
                if s[r] in chk:
                    cur+=1
                r+=1
            else:
                if s[l] in chk:
                    cur-=1
                l+=1
            ans = max(ans, cur)
        return ans
