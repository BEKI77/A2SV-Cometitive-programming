class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = ""
        n = len(strs)

        if n == 0:
            return ""
        if n == 1:
            return strs[0]
        if len(strs[0]) == 0:
            return strs[0]

        i = 0
        while i < len(strs[0]):
            cur = strs[0][i]
            cnt = 1

            for k in range(1, n):
                if i<len(strs[k]) and cur == strs[k][i]:
                    cnt += 1

            if cnt == n:
                ans += cur
            else:
                break

            i += 1

        return ans
