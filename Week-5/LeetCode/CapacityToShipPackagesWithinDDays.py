class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isVal(m,days):
            acc,day = 0,1
            i = 0
            while i<len(weights):
                if acc+weights[i]<=m:
                    acc+=weights[i]
                else:
                    day+=1
                    acc= weights[i]

                i+=1 

            return day<=days

        l , r = max(weights), sum(weights)
        ans = r

        while l<=r:
            m = l+ ((r-l)//2)
            if isVal(m, days):
                ans = m
                r = m-1
            else:
                l = m+1

        return ans