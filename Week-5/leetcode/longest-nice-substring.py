class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = []
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                ans.append(s[i:j+1])

        def isVal(st):
            temp = set(st)
            for i in temp:
                if i.isupper() and i.lower() not in temp:
                    return False
                elif i.islower() and i.upper() not in temp:
                    return False
            return True

        res, mx = '',0
        
        for i in ans:
            if isVal(i) and len(i)>mx:
                res = i
                mx = len(i)
       
        return res