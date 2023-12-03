class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = s.split()
        print(arr)
        mx = 0
        for i in range(len(arr)):
            mx = max(mx,len(arr[i]))
        ans = []
        for i in range(mx):
            cur=''
            for j in range(len(arr)):
                if i<len(arr[j]):
                    cur+=arr[j][i]
                else:
                    cur+=' '

            r = len(cur)-1
            while r>=0 and cur[r]==' ': r-=1
            ans.append(cur[0:r+1])

        return ans