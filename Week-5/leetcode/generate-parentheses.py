class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cur = []
        ans = set()
        def backtrack(opcnt, clocnt):
            nonlocal n
            if opcnt==n and clocnt==n:
                ans.add("".join(cur))
           
           
            if opcnt<n:
                cur.append('(')
                backtrack(opcnt+1, clocnt)
                cur.pop()

            if clocnt<opcnt:
                cur.append(')')
                backtrack(opcnt, clocnt+1)
                cur.pop()

        backtrack(0,0)
        return ans
