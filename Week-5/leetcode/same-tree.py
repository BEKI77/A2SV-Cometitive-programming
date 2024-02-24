# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        cnt1,cnt2 = 0 , 0
        def rec(p,li)->None:
            if p:
                li.append(p.val)
                rec( p.left,li)
                rec( p.right, li)
            else:
                li.append(None)
                return None
        li1 = []
        li2 = []
        rec(p,li1)
        rec(q,li2)
        print(li1,li2)
        return li1==li2