class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = { 2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'],
                6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z'] }
        cur = []
        ans = []
        def backtrack(i):
            nonlocal digits
            if len(cur)==len(digits):
                temp = "".join(cur)
                if temp !="":
                    ans.append(temp)
                return
            for k in mp[int(digits[i])]:
                cur.append(k)
                backtrack(i+1)
                cur.pop()

        backtrack(0)
    
        return ans