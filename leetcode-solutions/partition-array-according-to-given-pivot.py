class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        bigger=[]
        for i in nums:
            if i<pivot:
                less.append(i)
            elif i>pivot:
                bigger.append(i)
        piv = len(nums)-len(less)-len(bigger)
        ans = less
        for i in range(piv):
            ans.append(pivot)
        ans=ans+bigger
        return ans
