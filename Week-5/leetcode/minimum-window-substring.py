class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp1 = defaultdict(int)
        mp2 = defaultdict(int)
        for i in t:
            mp1[i]+=1

        required = len(mp1)
        l,formed, size = 0, 0,inf
        anl,anr = 0,0
        
        for r in range(len(s)):
            mp2[s[r]]+=1
            if s[r] in mp1 and mp2[s[r]] == mp1[s[r]]:
                formed+=1
            while formed == required:

                if r-l+1<size:
                    anl,anr= l , r
                    size = r-l+1
                mp2[s[l]]-=1
                if s[l] in mp1 and mp2[s[l]]<mp1[s[l]]:
                    formed -=1
                l+=1
        
        return "" if size==inf else s[anl:anr+1]

