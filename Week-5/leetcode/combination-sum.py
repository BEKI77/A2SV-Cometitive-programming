class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cur = []
        ans = []
        n = len(candidates)
        def backtrack(i):
            nonlocal target,n
            if sum(cur)==target:
                ans.append(cur.copy())
            if sum(cur)>target:
                return
            for j in range(i,n):
                cur.append(candidates[j])
                backtrack(j)
                cur.pop()
        backtrack(0)
        return ans