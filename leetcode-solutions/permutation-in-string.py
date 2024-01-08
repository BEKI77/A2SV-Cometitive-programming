class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m=len(s1),len(s2)
        if n>m:
            return False
        li1=[0]*26
        li2=[0]*26
        for i in range(len(s1)):
            li1[ord(s1[i])-ord('a')]+=1
            li2[ord(s2[i])-ord('a')]+=1
        if li1==li2:
            return True
        for i in range(n,m):
            li2[ord(s2[i])-ord('a')]+=1
            li2[ord(s2[i-n])-ord('a')]-=1
            if li1==li2:
                return True
        return False

















        # s1Table = Counter(s1)
        # i=0
        # while i<len(s2)-len(s1)+1:
        #     if Counter(s2[i:i+n])==s1Table:
        #         return True
        #     else:
        #         i+=1

        # return False