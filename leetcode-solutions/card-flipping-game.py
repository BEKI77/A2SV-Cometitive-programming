class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        fro=set()
        bac=set()
        mp=set()
        for i in range(len(fronts)):
            if fronts[i]!=backs[i]:
                fro.add(fronts[i])
                bac.add(backs[i])
            elif fronts[i]==backs[i]:
                if fronts[i] in fro:
                    fro.remove(fronts[i])
                if fronts[i] in bac:
                    bac.remove(fronts[i])
                mp.add(fronts[i])
        ans=float('inf')
        for i in bac:
            if i not in mp:
                ans=min(ans,i)
        for i in fro:
            if i not in mp:
                ans=min(ans,i)
        if ans==float('inf'):
            return 0
        else: return ans