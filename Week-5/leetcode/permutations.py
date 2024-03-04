class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        n = len(nums)
        def backtrack(start):
            nonlocal n
            if len(cur) == n:  
                ans.append(cur.copy())

            for i in range(n):
                if nums[i] not in cur:
                    cur.append(nums[i])
                    backtrack(i)
                    cur.pop()

        backtrack(0)
        return ans