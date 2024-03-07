class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l ,r = 0, len(citations)-1
        ans = l
        while l<=r:
            m = l + ((r-l)//2)
            if citations[m] < n-m:
                ans = m+1
                l = m+1
            else:
                r = m-1

        return len(citations[ans:])