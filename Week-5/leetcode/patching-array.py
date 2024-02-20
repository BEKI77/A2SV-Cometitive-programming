class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        curr_max = 0
        i = 0
        while curr_max < n:
            if i < len(nums) and nums[i] <= curr_max + 1:
                curr_max += nums[i]
                i += 1
            else:
                patches += 1
                curr_max += curr_max + 1

        return patches