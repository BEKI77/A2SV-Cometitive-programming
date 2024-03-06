class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        l,r = 0, max(houses[-1],heaters[-1])
        ans = r
        def isVal(m):
            pt1,pt2 = 0, 0

            while pt1<len(heaters) and pt2<len(houses):

                leftB, rightB = heaters[pt1]-m, heaters[pt1]+m

                if leftB <= houses[pt2] <= rightB:
                    pt2+=1
                elif houses[pt2]<leftB:
                    return False
                else:
                    pt1+=1

            return pt2 == len(houses)
            
        while l<=r:
            m = l+((r-l)//2)
            print(m, isVal(m))
            if isVal(m):
                ans = m
                r = m-1
            else:
                l = m+1
        return ans