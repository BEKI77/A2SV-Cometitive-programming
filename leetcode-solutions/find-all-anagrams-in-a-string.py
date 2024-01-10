class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ha = [0]*26
        dynamic = [0]*26
        ans = []
        if len(p)>len(s):
            return ans
        for i in range(len(p)):
            ha[ord(p[i])-ord('a')]+=1
            dynamic[ord(s[i])-ord('a')]+=1

        if dynamic==ha:
            ans.append(0)

        for i in range(len(p),len(s)):
            dynamic[ord(s[i])-ord('a')]+=1
            dynamic[ord(s[i-len(p)])-ord('a')]-=1
            if dynamic==ha:
                ans.append(i-len(p)+1)
        
        return ans
            