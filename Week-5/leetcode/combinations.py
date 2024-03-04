class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        cur = []
        def rec(ind,start):
            nonlocal k,n
            if ind==k:
                ans.append(cur.copy())
        
        
            for i in range(start+1,n+1):
                cur.append(i)
                rec(ind+1,i)
                cur.pop()
         
        rec(0,0)
        return ans