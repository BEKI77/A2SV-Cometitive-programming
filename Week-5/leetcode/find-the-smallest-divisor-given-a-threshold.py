class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isVal(m):
            nonlocal threshold
            temp =0
            for i in nums:
                temp+= math.ceil(i/m)           
            return temp<=threshold

        l, r = 1, max(nums)
        ans = r
        while l<=r:
            m = l + ((r-l)//2)
            if isVal(m):
                ans = m
                r = m-1
            else:
                l = m+1
        return ans