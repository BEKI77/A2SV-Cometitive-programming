class Solution:
    def largestGoodInteger(self, num: str) -> str:
        mx = -1
        for i in range(len(num)-2):
            if num[i]==num[i+1] and num[i]==num[i+2]:
                if int(num[i:i+3]) >= mx:
                    ans=num[i:i+3]
                    mx=int(num[i:i+3])
        if mx==-1:
            return ''
        else:  
            return ans