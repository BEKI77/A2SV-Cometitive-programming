# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def rec(root,val):
            if root and root.val == val:
                return root
            if root:
                return rec(root.left, val) or rec(root.right, val)
                
            else:
                return 
        
        return rec(root, val) 
