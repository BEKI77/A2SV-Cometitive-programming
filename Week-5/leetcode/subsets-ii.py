class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        cur = []
        ans = []
        chk = set()
        n = len(nums)
        def backtrack(start):
            nonlocal n
            temp = tuple(sorted(cur))
            if temp not in chk:
                ans.append(cur.copy())
                chk.add(temp)

            for i in range(start,n):
                cur.append(nums[i])  
                backtrack(i+1)
                cur.pop()

        backtrack(0)
        return ans