class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        ans,n = 0, len(arr)
        li = []
        for i in range(n+1):
            while li and (i==n or arr[li[-1]]>=arr[i]):
                cur = li.pop()
                left = li[-1] if li else -1
                right = i
                cnt = ((cur-left)*(right-cur))
                ans+= (arr[cur]*cnt)
                ans%=MOD
            li.append(i)
    
        return ans