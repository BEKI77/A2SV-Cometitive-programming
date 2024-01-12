class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        tot = sum(cardPoints)
        n = len(cardPoints)
        cur = sum(cardPoints[0:n-k])
        ans= tot-sum(cardPoints[0:n-k])
        
        for i in range(n-k,n):
            cur-=cardPoints[i-(n-k)]
            cur+=cardPoints[i]
            ans = max(ans, tot-cur)
                         
               
        return ans
