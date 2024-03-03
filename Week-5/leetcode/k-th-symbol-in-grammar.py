class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def rec(n,k):
            if n==1:
                return False
            if k>(2**n)//4:
                return not rec(n-1, (k-((2**n)//4)))
            else:
                return rec(n-1, k)

        return 1 if rec(n,k) else 0
