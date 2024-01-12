class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        arr = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i]%2:
                arr[i]=1
            else:
                arr[i]=0
        print(arr)
        pSum = [0]*len(nums)
        pSum[0]=arr[0]
        for i in range(1,len(nums)):
            pSum[i]= pSum[i-1]+arr[i]

        cntOfPr = defaultdict(int)
        
        for i in range(len(nums)):
            if pSum[i]==k:
                ans+=1
            if cntOfPr[pSum[i]-k]!=cntOfPr[-1]:
                ans+=cntOfPr[pSum[i]-k]  
            cntOfPr[pSum[i]]+=1 
        return ans