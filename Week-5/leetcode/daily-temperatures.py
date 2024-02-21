class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        li = []
        li.append(n-1)
        for i in range(n-2,-1,-1):
            while li and temperatures[li[-1]]<= temperatures[i]:
                li.pop()
            if not li:
                li.append(i)
                continue
            ans[i] = li[-1]-i
            li.append(i)

        return ans