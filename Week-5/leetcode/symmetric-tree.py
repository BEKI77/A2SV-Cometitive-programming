# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def rec(root1,root2):
            if (root1 and not root2) or (not root1 and root2):
                return False
            elif not root1 and not root2:
                return True  

           
            if root1.val==root2.val:
                return rec(root1.left, root2.right) and rec(root1.right, root2.left)
            else:
                return False
            
            

            
            
        return rec(root.left, root.right)