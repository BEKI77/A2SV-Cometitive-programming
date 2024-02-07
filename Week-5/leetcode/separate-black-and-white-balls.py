class Solution:
    def minimumSteps(self, s: str) -> int:
        r = len(s)-1
        cnt,ans = 0,0
        while r>=0:
            if s[r]=='0':
                cnt+=1
            else:
                ans+=cnt
            r-=1
        return ans