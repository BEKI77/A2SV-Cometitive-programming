class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        table=["qQwWeErRtTyYuUiIoOpP","aAsSdDfFgGhHjJkKlL","zZxXcCvVbBnNmM"]
        ans=[]
        for i in range(len(words)):
            cur,cnt=0,0
            if words[i][0] in table[0]:
                cur=0
            elif words[i][0] in table[1]:
                cur=1
            else:
                cur=2
            for j in range(len(words[i])):
                if  words[i][j] in table[cur]:
                    cnt+=1
            if cnt==len(words[i]):
                ans.append(words[i])
        return ans

        