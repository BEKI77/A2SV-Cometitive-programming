class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        if len(piles)==3: return sorted(piles)[1] 
        else:
            arr,ans = sorted(piles),0
            j=len(piles)-2
            i=0
            while i<len(piles)//3:
                ans+=arr[j]
                j-=2
                i+=1
            return ans
