class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        li = []
        for i in range(len(weights)-1):
            li.append(weights[i]+weights[i+1])
        li.sort()
        ans,n = 0, len(li)
        for i in range(k-1):
            ans+=li[n-i-1]-li[i]
        return ans