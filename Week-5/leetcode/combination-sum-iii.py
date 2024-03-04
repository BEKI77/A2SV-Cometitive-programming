class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        cur = []
        ans = []
        def backtrack(i):
            nonlocal k,n
            if len(cur) == k and sum(cur)==n:
                ans.append(cur.copy())
            if sum(cur)>n:
                return 
            for j in range(i,10):
                cur.append(j)
                backtrack(j+1)
                cur.pop()
        backtrack(1)
        return ans