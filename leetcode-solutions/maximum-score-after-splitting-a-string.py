class Solution:
    def maxScore(self, s: str) -> int:
        ans,cnt,cntz=0,0,0
        for i in s:
            if i=='1':
                cnt+=1
        for i in range(len(s)-1):
            if s[i]=='1':
                cnt-=1
            else:
                cntz+=1
            ans=max(ans, cntz+cnt)
        return ans
