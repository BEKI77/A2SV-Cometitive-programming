class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        arr = list(map(int,boxes))
        ans=[]
        for i in range(len(boxes)):
            cur=0
            for j in range(len(boxes)):
                if arr[j]==1:
                    cur+=abs(i-j)
            ans.append(cur)
        return ans