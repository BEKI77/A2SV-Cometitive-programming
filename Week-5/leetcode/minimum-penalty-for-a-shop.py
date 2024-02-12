class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pSum = [0]*(len(customers)+1)
        for i in range(len(customers)):
            if customers[i]=='Y':
                pSum[i+1]=pSum[i]+1
            else:
                pSum[i+1]=pSum[i]
        ans,mx = 0,inf
        for i in range(len(customers)+1):
            key = (pSum[-1]-pSum[i])+(i-pSum[i])
            if key<mx:
                mx = key
                ans = i
        return ans
        