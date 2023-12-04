class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans=0
        cur = capacity
        for i in range(len(plants)):
            if cur - plants[i]>=0:
                ans+=1
                cur-=plants[i]
            else:
                cur=capacity - plants[i]
                ans+= 2*(i)+1
                

        return ans