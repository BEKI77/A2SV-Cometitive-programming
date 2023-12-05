class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n=max(candies)
        ans=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies >= n:
                ans.append(True)
            else:
                ans.append(False)
        return ans