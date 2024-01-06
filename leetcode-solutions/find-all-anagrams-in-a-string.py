class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hash = Counter(p)
        ans = []
        for i in range(len(s)-len(p)+1):
            temp = Counter(s[i:i+len(p)])
            if temp==hash:
                ans.append(i)
        return ans
            