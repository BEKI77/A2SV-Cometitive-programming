class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(s)):
            mp[s[i]]=i
        ans = []
        start = end = 0
        for i in range(len(s)):
            end = max(end, mp[s[i]])
            if end == i:
                ans.append(end-start+1)
                start=end+1
        return ans