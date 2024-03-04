# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        def rec(l,r):
            if l>r:
                return None
            m = (l+r)//2 
            return TreeNode(nums[m], rec(l,m-1), rec(m+1,r))

        return rec(0,n-1)