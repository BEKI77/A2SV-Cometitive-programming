class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1[0]=='0' or num2[0]=='0':
            return '0'
        n = len(num1)+len(num2)+1
        arr=[0]*n
        
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                arr[i+j+1] += int(num1[i])*int(num2[j])
                arr[i+j] += arr[i+j+1]//10
                arr[i+j+1] %=10

        i=0
        while arr[i]==0 : i+=1
        ans = ''
        while i<n-1:
            ans+=str(arr[i])
            i+=1
        return ans
