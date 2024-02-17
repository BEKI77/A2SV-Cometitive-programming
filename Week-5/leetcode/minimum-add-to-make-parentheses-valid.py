class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ope,val,clo = 0,0,0
        for i in range(len(s)):
            if s[i]=='(':
                ope+=1
            elif ope>0 and s[i]==')':
                ope-=1 
                val+=1
        print(val)
        return len(s) - (2*val)