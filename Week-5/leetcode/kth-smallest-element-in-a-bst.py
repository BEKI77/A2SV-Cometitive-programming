# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        li = []
        def rec(root):
            nonlocal li
            if not root or len(li)>k:
                return
            rec(root.left)
            li.append(root.val)
            rec(root.right)
        rec(root)
        return li[k-1]