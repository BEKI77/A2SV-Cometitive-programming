import bisect as bisect
n = int(input())
shops = sorted(map(int,input().split()))
q = int(input())
mon = []
for _ in range(q):
    val = bisect.bisect_right( shops , int(input()))
    print(val)
