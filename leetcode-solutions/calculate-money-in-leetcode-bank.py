class Solution:
    def totalMoney(self, n: int) -> int:
        ans=0
        if n<8:
            for i in range(n):
                ans+=1+i
        else:
            cur=0
            for i in range(n//7):
                for j in range(7):
                    ans+=i+j+1
                cur=i
            cur+=1
            for i in range(n%7):
                ans+=cur+1+i
        return ans
