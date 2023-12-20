class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans=0
        for c in range(len(strs[0])):
            cur=False
            for r in range(len(strs)-1):
                if strs[r][c] > strs[r+1][c]:
                    cur=True
                    break
            if cur:
                ans+=1
        return ans