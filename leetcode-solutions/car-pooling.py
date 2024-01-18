class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = max(trips, key = lambda x:x[-1])[-1]
        sPep = [0]*(n+1)
        for pep, l, r in trips:
            sPep[l] += pep
            sPep[r] -= pep
        for i in range(1,n+1):
            if sPep[i-1]>capacity:
                return False
            sPep[i]+=sPep[i-1]
        return True