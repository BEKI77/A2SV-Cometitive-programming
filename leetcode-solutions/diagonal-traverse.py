class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        r = len(mat)
        c = len(mat[0])
        res=defaultdict(list)
        for i in range(r):
            for j in range(c):
                res[i+j].append(mat[i][j])
        ans=[]
        for i in range(r+c):
            if i%2:
                for j in range(len(res[i])):
                    ans.append(res[i][j])
            else:
                for j in range(len(res[i])-1,-1,-1):
                    ans.append(res[i][j])
        return ans