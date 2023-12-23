class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n<3:
            return False
        t=0
        while t+1<n and arr[t]<arr[t+1]:
            t+=1
        if t+1==n or t==0:
            return False
        while t+1<n and arr[t]>arr[t+1]:
            t+=1
        return t+1==n
            

            
        
     
