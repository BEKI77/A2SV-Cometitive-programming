class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        temp = abs(n)
        while temp!=0:
            if temp&1 != 0:
                ans*=x
            x*=x
            temp>>=1
        return ans if n>0 else 1 if n==0 else 1/ans