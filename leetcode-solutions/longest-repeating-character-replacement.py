class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        table = [0]*26
        ans,maxF = 0,0
        l,r=0,0
        while r<len(s):
            table[ord(s[r])-ord('A')]+=1
            maxF = max(maxF, table[ord(s[r])-ord('A')])
            if (r-l+1) - maxF > k:
                table[ord(s[l])-ord('A')]-=1
                l+=1
            else:
                ans = max(ans, (r-l+1))
            r+=1
        return ans