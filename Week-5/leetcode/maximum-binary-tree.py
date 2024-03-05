# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(l,r):
            if l<r:
                mx = max(nums[l:r])
                ind = nums.index(mx)
                return TreeNode(mx, rec(l,ind), rec(ind+1, r))
            else:
                return None
        return rec(0,len(nums))