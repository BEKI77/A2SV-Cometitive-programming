class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur = []
        ans = []
        n = len(nums)
        def backtrack(start):
            nonlocal n
            ans.append(cur.copy())

            for i in range(start,n):
                cur.append(nums[i])  
                backtrack(i+1)
                cur.pop()

        backtrack(0)
        return ans