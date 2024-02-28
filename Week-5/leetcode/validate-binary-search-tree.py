# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(root,curMin, curMax):
            if root and (root.val<=curMin or root.val>=curMax):
                return False
            
            if root:
                return rec(root.left,curMin,root.val) and rec(root.right, root.val,curMax)
            
            return True

        return rec(root,-inf,inf)