# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def rec(root , p, q):
            if root and (root.val==p.val or root.val==q.val):
                return root
            elif root and root.val > p.val and root.val>q.val:
                return rec(root.left, p, q)
            elif root and root.val<p.val and root.val<q.val:
                return rec(root.right, p, q)
            elif root and ((root.val>p.val and root.val<q.val) or (root.val<p.val and root.val>q.val)):
                return root
            
            
            
        return rec(root, p ,q)