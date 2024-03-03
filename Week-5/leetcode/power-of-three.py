class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def rec(n):
            if n ==1.0:
                return True
            if n<1:
                return False
            else:
                return rec(n/3)

        return rec(n)