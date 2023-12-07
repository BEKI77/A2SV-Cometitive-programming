class Solution:
    def largestOddNumber(self, num: str) -> str: 
        ans=""
        for i in range(len(num)-1,-1,-1):
            cur = int(num[i])
            if cur%2!=0:
                ans = num[0:i+1]
                break
                     
        return ans