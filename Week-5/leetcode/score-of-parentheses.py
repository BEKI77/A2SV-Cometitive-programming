class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        li = []
        ans,val = 0,0
        for i in range(len(s)):
            temp = s[i]
            if temp=='(':
                li.append(0)
            else:
                mul = li[-1]
                li.pop()
                if mul==0:
                    val = 1
                else:
                    val = mul*2
                
                if not li:
                    ans+=val
                else:
                    cur = li[-1]+val
                    li.pop()
                    li.append(cur)
        return ans
