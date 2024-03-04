class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cur = []
        li = set()
        ans = []
        n = len(candidates)
        candidates.sort()

        def backtrack(i):
            nonlocal target,n
            if sum(cur)>target:
                return

            if sum(cur)==target:
               ans.append(cur.copy())
                 
            j = i
            while j<n:
                cur.append(candidates[j])
                backtrack(j+1)
                cur.pop()
                while j<n-1 and candidates[j]==candidates[j+1]:
                    j+=1
                j+=1
        
        backtrack(0)
        return ans