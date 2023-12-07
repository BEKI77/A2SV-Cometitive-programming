class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ''
        cur=0
        for i in range(len(s)):
            if cur<len(spaces) and i<spaces[cur]:
                ans+=s[i]
            elif cur<len(spaces):
                ans+=' '
                ans+=s[i]
                cur+=1
            elif i>spaces[cur-1]:
               ans+=s[i]
        return ans
