class Solution:
    def reverseWords(self, s: str) -> str:
        temp = list(s.split())
        return ' '.join(reversed(temp))