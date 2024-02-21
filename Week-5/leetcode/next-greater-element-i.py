class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        dic = { nums1[i] : i  for i in range(len(nums1))}
        li = []
        for i in range(len(nums2)):
            while len(li) > 0 and li[-1] < nums2[i]:
                ans[dic[li.pop()]] = nums2[i]
                
            if nums2[i] in dic:
                li.append(nums2[i])
        return ans
        