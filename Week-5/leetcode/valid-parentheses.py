class Solution:
    def isValid(self, s: str) -> bool:
        li = []
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                li.append(s[i])
            elif s[i]==')' and li and li[-1]=='(':
                li.pop()
            elif s[i]=='}'and li and li[-1]=='{':
                li.pop()
            elif s[i]==']' and li and li[-1]=='[':
                li.pop()
            else:
                return False

        return True if not li else False