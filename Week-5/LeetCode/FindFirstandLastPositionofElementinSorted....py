class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect.bisect_left(nums, target, lo=0, hi=len(nums))
        r = bisect.bisect_right(nums, target, lo=0, hi=len(nums))
        if l<len(nums) and r-1<len(nums) and nums[l]==nums[r-1] and nums[l]==target:
            return [l,r-1]
        else:
            return [-1,-1]