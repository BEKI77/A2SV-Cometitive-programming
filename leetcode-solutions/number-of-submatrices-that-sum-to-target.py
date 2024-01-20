class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        for r in matrix:
            for i in range(1,len(r)):
                r[i]+=r[i-1]
        ans=0
        for c1 in range(len(matrix[0])):
            for c2 in range(c1,len(matrix[0])):
                mp = defaultdict(int)
                mp[0]=1
                cur=0
                for r in range(len(matrix)):
                    cur += matrix[r][c2] - (matrix[r][c1-1] if c1>0 else 0)
                    if cur-target in mp:
                        ans+=mp[cur-target]
                    mp[cur]+=1
        return ans
