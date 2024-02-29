# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        li = []
        def rec(root,val):
            if root and not root.right and not root.left:
                return li.append(val+str(root.val))

            if root and root.left and root.right:           
                rec(root.left, val+str(root.val))
                rec(root.right, val+str(root.val))
            elif root and root.left:
                rec(root.left, val+str(root.val))
            elif root and root.right:
                rec(root.right, val+str(root.val))

        rec(root, '')
    
        return sum( int(i) for i in li)