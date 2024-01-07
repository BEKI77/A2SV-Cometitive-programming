class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        ans,cur=0,0
        l,r=0,0
        cntF=0
        while l<n and r<n:
            if cntF<=k and answerKey[r]=="T":
                ans = max(ans,r-l+1)
                r+=1
            elif cntF<k and answerKey[r]=="F":
                ans = max(ans,r-l+1)
                cntF+=1
                r+=1 
            else:
                if answerKey[l]=="F":
                    cntF-=1
                l+=1     
     
        l,r = 0,0
        cntT=0
        while l<n and r<n:
            if cntT<=k and answerKey[r]=="F":
                ans = max(ans,r-l+1) 
                r+=1
            elif cntT<k and answerKey[r]=="T":
                ans = max(ans,r-l+1)
                cntT+=1
                r+=1    
            else:
                if answerKey[l]=="T":
                    cntT-=1
                l+=1  
   
        return ans