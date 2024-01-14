class Solution:
    def balancedString(self, s: str) -> int:
        ta = Counter(s)
        remove = {}
        n=len(s)//4
        for i in ta:
            if ta[i]>n:
                remove[i]=ta[i]-n
        if not remove:
            return 0
        ans=len(s)
        l=0
        for r in range(len(s)):
            if s[r] in remove:
                remove[s[r]] -=1
            
            while max(remove.values())<=0:
                    ans = min(ans,r-l+1)
                    if s[l] in remove:
                        remove[s[l]]+=1
                    l+=1
                
        return ans
