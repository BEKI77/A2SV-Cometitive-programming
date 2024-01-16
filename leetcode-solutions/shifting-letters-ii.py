class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        psum = [0]*(len(s)+1)
        alp = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(len(shifts)):
            if shifts[i][2]:
                psum[shifts[i][0]]+=1
                psum[shifts[i][1]+1]-=1
            else:
                psum[shifts[i][0]]-=1
                psum[shifts[i][1]+1]+=1
        for i in range(1,len(psum)): psum[i] = psum[i]+psum[i-1]
        res = list(s)

        for i in range(len(res)):
            va = ((ord(res[i])-ord('a') + psum[i])%26)%26
            res[i] = alp[va]
            
        return ''.join(res)