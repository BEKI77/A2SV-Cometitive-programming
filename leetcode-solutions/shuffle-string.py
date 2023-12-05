class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans=list(s)
        for  i,val in enumerate(indices,0):
            ans[val]=s[i]
        
        return ''.join(ans)