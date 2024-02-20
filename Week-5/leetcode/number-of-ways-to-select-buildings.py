class Solution:
    def numberOfWays(self, s: str) -> int:
        ans = 0
        ones,zeros = 0,0
        prev_zeros, prev_ones = 0,0
        for i in s:
            if i == '1':
                ans += prev_ones
                prev_zeros += zeros
                ones += 1
            else:
                ans += prev_zeros
                prev_ones += ones
                zeros += 1
        return ans