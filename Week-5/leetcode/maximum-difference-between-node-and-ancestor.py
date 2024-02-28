# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
    
        def rec(root, lMax, lMin)->int:
            if not root:
                return  (lMax-lMin)
            lMin = min(lMin, root.val) 
            lMax = max(lMax, root.val)
            return max(rec(root.left, lMax, lMin), rec(root.right, lMax, lMin))     
      
        return rec(root, 0, inf)