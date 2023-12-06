class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        ans = []
        for i,val in freq.items() :
           if val > len(nums)//3:
               ans.append(i)
        return ans
