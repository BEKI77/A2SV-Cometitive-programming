class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(len(nums)):
            r= i+nums[i]
            if i==(r%n)%n:
                continue
            visited=set()
            while (r%n)%n!= i and (r%n)%n not in visited and nums[i]*nums[(r%n)%n]>=0:
                visited.add((r%n)%n)
                r=r+nums[(r%n)%n]
            if (r%n)%n==i:
                return True
        return False

            

       
            


            

            
            
            
                
