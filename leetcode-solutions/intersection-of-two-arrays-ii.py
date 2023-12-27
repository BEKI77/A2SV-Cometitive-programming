class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        chk = Counter(nums2)
        ans = []
        for i in range(len(nums1)):
            if chk[nums1[i]]>0:
                ans.append(nums1[i])
                chk[nums1[i]]-=1
        return ans