class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        def pow(a,b,mod):
            if b == 0:
                return 1
            half_pow = pow(a,b//2,mod)
            if b%2 :
                return (half_pow * half_pow * a ) % mod
            return (half_pow*half_pow)%mod

        x = n // 2
        even = pow(5,x,MOD)
        odd = pow(4,x,MOD)

        if n%2:
            return (odd * even * 5) % MOD
        return (odd * even ) % MOD