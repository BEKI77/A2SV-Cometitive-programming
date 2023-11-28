class Solution:
    def isPalindrome(self, x: int) -> bool:
      num = str(x)
      if x<0:
          return False
      l,r = 0,len(num)-1
      while(l<=r):
        if num[l]!=num[r]:
            return False
        l=l+1
        r=r-1 
      
      return True
        