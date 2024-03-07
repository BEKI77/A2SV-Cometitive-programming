class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        li = [[abs(i-x), i] for i in arr]
        li.sort(key = lambda x: (x[0],x[1]))
        # print(li)
        ans = []
        for i in range(k):
            ans.append(li[i][1])
        return sorted(ans)