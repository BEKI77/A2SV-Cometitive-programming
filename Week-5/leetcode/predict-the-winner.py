class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def rec( l, r, nums, turn)->int:
            if l>r: return 0

            if turn==0:
                return max((nums[l]+ rec(l+1, r, nums, 1 )), nums[r]+rec(l, r-1, nums, 1))
            else:
                return min((-nums[l]+rec(l+1, r, nums, 0)), -nums[r]+rec(l,r-1, nums, 0))
        

        return rec(0,len(nums)-1, nums ,0)>=0