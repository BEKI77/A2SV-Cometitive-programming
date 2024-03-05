# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        li = []
        def rec(root):
            if root:
                rec(root.left)
                li.append(root.val)
                rec(root.right)
                return
        rec(root)
        def builder(l,r):
            if l<=r:
                m = l+((r-l)//2)
                return TreeNode(li[m], builder(l,m-1), builder(m+1, r)) 
            else:
                return None
        return builder(0,len(li)-1)