# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def sum(root,i)->int:
            if root and root.val>=low and root.val<=high:
                i+=root.val+sum(root.left,i)+sum(root.right,i)
                return i
            elif root and root.val<low:
                return i+sum(root.right,i)
            elif root and root.val>high:
                return i+sum(root.left,i)
            else:
                return 0
        return sum(root,0)