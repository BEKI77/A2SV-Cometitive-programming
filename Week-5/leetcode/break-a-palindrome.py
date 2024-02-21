class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)<=1:
            return ""
            
        li = list(palindrome)
        fl = False
        for i in range(len(li)//2):
            if li[i]>'a':
                li[i]='a'
                fl = True
                break
        if fl:
            ans = ''.join(li)
        else:
            li[-1]='b'
            ans = ''.join(li)
        return ans 
        

        