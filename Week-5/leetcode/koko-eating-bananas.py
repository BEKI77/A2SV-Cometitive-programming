class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        ans = r
        def isVal(m):
            nonlocal h
            taken = 0
            for i in range(len(piles)):
                temp= piles[i]
                taken+= temp//m
                temp = temp%m
                if temp>0:
                    taken+=1
                if taken>h:
                    return False        
            return True
           
        while l<=r:
            m = l+((r-l)//2)
            if isVal(m):
                ans = m
                r= m-1
            else:
                l = m+1

        return ans