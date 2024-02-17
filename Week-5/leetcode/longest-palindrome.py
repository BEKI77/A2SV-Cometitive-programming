class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = Counter(s)
        ans = 0
        mx = 0
        for i in mp:
            ans+= mp[i]-(mp[i]%2)
            mx = max(mx,(mp[i]%2))
            
        return ans+mx