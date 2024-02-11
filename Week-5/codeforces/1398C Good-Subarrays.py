from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input()))
    pSum = [0]*(n+1)
    for i in range(n):
        pSum[i+1]=pSum[i]+arr[i]
    ans = 0
    dic = defaultdict(int)
    for i in range(0,n+1):
        ans+=dic[pSum[i]-i]
        dic[pSum[i]-i]+=1
    
    print(ans)