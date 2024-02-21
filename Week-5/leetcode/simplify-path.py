class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        li =  []
        i=0
        while i<n:
            while i<n and path[i]=='/':
                i+=1

            if i == n:
                break
                
            temp = ''
            while i<n and path[i]!='/':
                temp+=path[i]
                i+=1

            if temp=='.':
                None
            elif temp == '..':
                if li:
                    li.pop()
            else:
                li.append('/'+temp)


        return "".join(li) if li else '/'