class Solution:
    def sortSentence(self, s: str) -> str:   
        return ' '.join(i[:len(i)-1] for i in sorted(list(s.split()),key = lambda x:x[len(x)-1]))